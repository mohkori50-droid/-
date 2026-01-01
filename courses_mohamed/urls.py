from django.contrib import admin
from django.urls import path
from . import views  # استيراد الـ views مباشرة لأنها في نفس المجلد

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.course_list, name='course_list'),  # تأكد من اسم الدالة في views.py
    path('course/<int:pk>/', views.video_detail, name='video_detail'),
]