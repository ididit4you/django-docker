#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "DEVELOP"
    exec python src/manage.py runserver 0.0.0.0:8000

else
    echo "PRODUCTION" 
    exec gunicorn src/project.wsgi:application -w 2 -b :8000
fi
