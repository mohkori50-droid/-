import os
from django.core.wsgi import get_wsgi_application

# تم تغيير core إلى courses_mohamed لتتوافق مع اسم مجلدك
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courses_mohamed.settings')

application = get_wsgi_application()