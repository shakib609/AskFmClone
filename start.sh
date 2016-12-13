#! /bin/bash

# Start gunicorn processes

echo Starting Gunicorn Webserver.
exec gunicorn config.wsgi:application \
     --bind 0.0.0.0:8000
     --workers 3
