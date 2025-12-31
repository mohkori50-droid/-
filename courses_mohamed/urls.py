from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.video_detail, name='video_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)