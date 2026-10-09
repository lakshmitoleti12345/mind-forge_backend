#!/usr/bin/env bash
# Render Build Script for Django Backend
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mindforge_backend.settings'); django.setup(); from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@mindforge.com', 'MindForgeAdmin123!')"
python manage.py runserver 8000 &
sleep 3
curl -X POST http://127.0.0.1:8000/api/seed/
