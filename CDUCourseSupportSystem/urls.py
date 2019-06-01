from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'CDUCourseSupportSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('student/', include(('student.urls', 'student'))),
    path('lecturer/', include(('lecturer.urls', 'lecturer'))),
    #url(r'^StudyPlan', include('student.urls'))
]

if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)