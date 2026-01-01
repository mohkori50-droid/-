from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    
    # تأكد أن الاسم هنا هو 'course_detail' ليتوافق مع زر الـ HTML
    # وتأكد أنه يستدعي دالة 'video_detail' الموجودة في الـ views
    path('course/<int:course_id>/', views.video_detail, name='course_detail'),
]