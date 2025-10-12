# Deployment Guide for Social Media API

## Production Configuration

This Django REST API is configured for production deployment with the following settings:

### Security Settings
- DEBUG = False - Disabled debug mode for production
- ALLOWED_HOSTS - Configured via environment variables
- SECURE_BROWSER_XSS_FILTER = True - XSS protection enabled
- X_FRAME_OPTIONS = DENY - Clickjacking protection
- SECURE_CONTENT_TYPE_NOSNIFF = True - MIME type sniffing protection
- SECURE_SSL_REDIRECT - Can be enabled for HTTPS

### Database Configuration
- Uses dj-database-url for flexible database configuration
- Supports PostgreSQL, MySQL, SQLite via DATABASE_URL environment variable
- Connection pooling enabled with conn_max_age=600

### Static Files
- Configured with WhiteNoise for efficient static file serving
- collectstatic command ready for deployment
- Compressed manifest storage for optimized delivery

### Environment Variables Required

SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=postgres://user:password@host:port/dbname

### Deployment Steps

1. Install dependencies
pip install -r requirements.txt

2. Set environment variables on your hosting platform

3. Run migrations
python manage.py migrate

4. Collect static files
python manage.py collectstatic --noinput

5. Start with Gunicorn
gunicorn social_media_api.wsgi

### Hosting Platforms
This application can be deployed to:
- Heroku
- AWS Elastic Beanstalk
- DigitalOcean
- Google Cloud Platform
- Any platform supporting Python/Django

### Media Files
For production, consider using cloud storage like AWS S3 or Google Cloud Storage for user-uploaded media files.