from .common import *
import dj_database_url

# Turning off debug in production
DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']

# Get database settings from heroku environment
DATABASES['default'] = dj_database_url.config(conn_max_age=500)

# Static File specific changes for heroku deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
