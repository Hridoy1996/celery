# to know about each line 
# https://coderbook.com/@marcus/best-practices-for-setting-up-celery-with-django/
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
'''
We set a default value for the DJANGO_SETTINGS_MODULE environment variable 
to be the python path to our settings file. This environment variable is used 
by Django to define which settings file it should load and it will allow us 
importing the settings with from django.conf import settings.
'''
app = Celery('proj')
'''
We instantiate the Celery instance to app variable and name our 
Celery application "tasks".
'''
app.config_from_object('django.conf:settings', namespace='CELERY')
'''
We load the Celery config values from the settings object within 
django.conf. This is where we will expect all of our configuration
to be set. The namespace="CELERY" means that we expect the configuration 
values that are related to Celery to be prefixed with CELERY_ so that
it does not clash with other Django settings.
'''

app.autodiscover_tasks()

'''
We use autodiscover_tasks() to tell Celery
that it should use the settings.INSTALLED_APPS list of applications to 
find defined Celery tasks. This allows us to split out the tasks
throughout our project’s code base where they logically belong.
'''