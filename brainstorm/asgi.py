import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "brainstorm.settings")
django.setup()
applicaton = get_default_application()