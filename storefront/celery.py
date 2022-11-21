import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','storefront.settings')

celery = Celery('storefront')
celery.config_from_object('django.conf:setting', namespace='CELERY')
celery.autodiscover_tasks()