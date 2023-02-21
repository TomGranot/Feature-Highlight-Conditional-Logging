from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

if (os.environ['DJANGO_ENV'] == "prod") or (os.environ['DJANGO_ENV'] == "production"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings.dev")
    
app = Celery('myapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)