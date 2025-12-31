from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الكورس")
    description = models.TextField(verbose_name="وصف الكورس")
    image = models.ImageField(upload_to='course_images/', verbose_name="صورة الكورس")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    # تم تصحيح الكلمة هنا من on_connection إلى on_delete
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE, verbose_name="الكورس")
    title = models.CharField(max_length=200, verbose_name="عنوان الدرس")
    video_url = models.URLField(verbose_name="رابط الفيديو (YouTube/Vimeo)")
    order = models.PositiveIntegerField(default=0, verbose_name="ترتيب الدرس")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"