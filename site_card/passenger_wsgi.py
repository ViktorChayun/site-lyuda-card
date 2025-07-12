import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

# Встановлюємо змінну середовища Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_card.settings")

# Імпортуємо wsgi з Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
