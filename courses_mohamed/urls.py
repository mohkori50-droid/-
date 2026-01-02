from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.course_list, name='course_list'),
    path('video/<int:course_id>/', views.video_detail, name='video_detail'), # هذا السطر كان ناقصاً
]