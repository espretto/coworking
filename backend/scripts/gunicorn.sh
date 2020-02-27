#!/bin/bash

gunicorn config.wsgi:application \
  --workers 4 \
  --worker-class gevent \
  --bind 0.0.0.0:5678 \
  --chdir=/backend \
  --log-level=info
