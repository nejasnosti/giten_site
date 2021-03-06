"""
WSGI config for gitensite project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os
import dotenv


try:
    dotenv.read_dotenv(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
except Exception as e:
    print(e)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gitensite.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
