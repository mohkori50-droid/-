from django.shortcuts import render, get_object_or_404
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def video_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # هذا السطر يفتح صفحة الفيديو مباشرة ويتجاهل أي تفعيل قديم
    return render(request, 'video_detail.html', {'course': course})