import os
import sys

# Add your project's directory the PYTHONPATH
path = 'C:\\Coding\\Fake-News-Detection\\src\\web\\fnews'
if path not in sys.path:
    sys.path.append(path)

# Move to the project directory
os.chdir(path)

# Tell Django where the settings.py module is located
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'fnews.settings'

)
# Set up Django -- let it instantiate everything!
import django
django.setup()

# Import the Django WSGI to handle requests
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()