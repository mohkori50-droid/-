from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.course_list, name='course_list'),
    path('video/<int:course_id>/', views.video_detail, name='video_detail'), # هذا السطر كان ناقصاً
]
from django.contrib.auth.models import User

# كود مؤقت لإنشاء مستخدم آلياً
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '12345678')