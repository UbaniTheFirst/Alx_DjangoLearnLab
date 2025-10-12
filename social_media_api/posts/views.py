from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors to edit or delete their own objects.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author
        return obj.author == request.user


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
def feed_view(request):
    """
    Return posts from users that the current user follows,
    ordered by creation date (most recent first)
    """
    if not request.user.is_authenticated:
        return Response(
            {'error': 'Authentication required'}, 
            status=401
        )
    
    # Get users that the current user follows
    following_users = request.user.following.all()
    
    # Get posts from those users, ordered by creation date
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    # Paginate the results
    paginator = StandardResultsSetPagination()
    paginated_posts = paginator.paginate_queryset(posts, request)
    
    # Serialize the posts
    serializer = PostSerializer(paginated_posts, many=True)
    
    return paginator.get_paginated_response(serializer.data)
