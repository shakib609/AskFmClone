from .common import *
import dj_database_url

# Turning off debug in production
DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']

# Get database settings from heroku environment
DATABASES['default'] = dj_database_url.config(conn_max_age=500)
