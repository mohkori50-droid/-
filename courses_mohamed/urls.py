from django.urls import path
from . import views  # استيراد ملف views.py الخاص بك

urlpatterns = [
    # الرابط الأساسي الذي تظهر فيه الكروت النيون
    path('', views.course_list, name='course_list'),

    # الرابط الجديد الذي سيفعل زر "فتح البيانات" لكل درس
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
]