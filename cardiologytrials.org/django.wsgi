import os
import sys

sys.path.append('/home/james/sites/cardiologytrials.org/django_cardiologytrials') 
sys.path.append('/home/james/sites/cardiologytrials.org') 

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_cardiologytrials.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
