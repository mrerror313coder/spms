"""
WSGI config for spms project.
"""

import os
import sys
from dotenv import load_dotenv

# Add your project directory to the sys.path
path = '/home/Asad313/spms'
if path not in sys.path:
    sys.path.append(path)

# Load environment variables
project_folder = os.path.expanduser(path)
load_dotenv(os.path.join(project_folder, '.env'))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spms.settings')

# Import Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
