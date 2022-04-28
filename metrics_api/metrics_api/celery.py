from __future__ import absolute_import
import os
from re import A
from celery import Celery

from celery.schedules import crontab # scheduler

# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metrics_api.settings')

app = Celery('metrics_api')

app.conf.timezone = 'UTC'

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'every-300-seconds': {
        'task': 'cable_diameter_api.tasks.get_cable_data',
        'schedule': 300,
    }
}

app.autodiscover_tasks()
