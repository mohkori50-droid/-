import os
from pathlib import Path

# 1. تعريف BASE_DIR بشكل صحيح
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. إعدادات الأمان
SECRET_KEY = 'django-insecure-your-key-here'
DEBUG = True  # اجعلها False عند الانتهاء تماماً
ALLOWED_HOSTS = ['*']

# 3. التطبيقات المسجلة (تأكد من إضافة تطبيقك و whitenoise)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses_mohamed',  # تطبيقك الخاص
    'whitenoise.runserver_nostatic', 
]

# 4. الوسيط (Middleware) - الترتيب هنا هو سر حل خطأ 500
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # هذا مكانه الصحيح
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 5. إعدادات الملفات الثابتة والميديا
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 6. تفعيل WhiteNoise للتخزين
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 7. إعدادات قاعدة البيانات والمنفذ
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
PORT = os.environ.get('PORT', '10000')

# أضف هذا السطر في نهاية الملف لربط المنفذ بـ Django
# WSGI_APPLICATION = 'courses_mohamed.wsgi.application'