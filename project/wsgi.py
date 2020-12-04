import os

from django.core.wsgi import get_wsgi_application
import os.path
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()
