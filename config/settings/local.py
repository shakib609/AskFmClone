from .common import *
import dj_database_url


# Set DEBUG to True for local development
DEBUG = True
ALLOWED_HOSTS = []

# Default database sqlite3
DATABASES['default'] = dj_database_url.config(
    default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
    conn_max_age=500
)
