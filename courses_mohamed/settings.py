STATIC_URL = 'static/'
# أضف هذا السطر لضمان عمل ملفات الـ CSS والـ Matrix على Render
STATIC_ROOT = BASE_DIR / 'staticfiles'

# تعاريف الميديا - سليمة تماماً
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# إضافة هامة جداً لـ Render لإصلاح خطأ الـ Port
import os
PORT = os.environ.get('PORT', '8000')