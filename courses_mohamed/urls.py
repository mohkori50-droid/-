from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. مسار لوحة الإدارة
    path('admin/', admin.site.urls),
    
    # 2. مسار نظام الحسابات الجاهز
    path('accounts/', include('django.contrib.auth.urls')), 
    
    # 3. المسار الرئيسي للتطبيق
    path('', include('courses_mohamed.urls')), 
]

# 4. الربط الحيوي لملفات الميديا والصور (مهم جداً لعمل الفيديوهات)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)