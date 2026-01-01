urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    # قمنا بتغيير 'courses.urls' إلى 'courses_mohamed.urls'
    path('', include('courses_mohamed.urls')), 
]