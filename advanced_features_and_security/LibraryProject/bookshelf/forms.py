from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    Example form for Book model demonstrating secure form handling.
    Uses Django's ModelForm for automatic validation and security.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name'
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter publication year'
            }),
        }
    
    def clean_publication_year(self):
        """
        Validate publication year to prevent invalid data.
        """
        year = self.cleaned_data.get('publication_year')
        if year and year < 1000:
            raise forms.ValidationError('Publication year must be valid.')
        return year