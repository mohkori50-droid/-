from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # هذا السطر هو الذي سيحل مشكلة 'login' فوراً
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', include('courses.urls')), # تأكد من اسم تطبيقك هنا
]