import os
from pathlib import Path

# 1. تعريف BASE_DIR بشكل صحيح (يجب أن يكون في أعلى الملف)
BASE_DIR = Path(__file__).resolve().parent.parent

# ... (باقي إعدادات Django مثل SECRET_KEY و INSTALLED_APPS)

# 2. إعدادات الملفات الثابتة (Static Files)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 3. إعدادات ملفات الميديا (Media Files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 4. تفعيل WhiteNoise (ضروري جداً لعمل التصميم على Render)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 5. إعدادات قاعدة البيانات التلقائية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 6. جلب المنفذ (Port) لإصلاح خطأ 503 و Port scan timeout
PORT = os.environ.get('PORT', '10000')