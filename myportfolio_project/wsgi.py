import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio_project.settings")

application = get_wsgi_application()

# 👇 Add this line for Vercel
app = application