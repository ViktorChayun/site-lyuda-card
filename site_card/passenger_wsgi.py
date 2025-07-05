import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_card.settings")


from django.core.wsgi import get_wsgi_application
# wsgi = imp.load_source('wsgi', 'manage.py')
# application = wsgi.wsgi.py
application = get_wsgi_application()
