#!/bin/bash
export DJANGO_SETTINGS_MODULE=app.conf.prod

exec gunicorn app.wsgi:application \
    --name app \
    --bind 0.0.0.0:5000 \
    --preload \
    --chdir='./' \
    --workers 2
