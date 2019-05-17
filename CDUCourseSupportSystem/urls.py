from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'CDUCourseSupportSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('student/', include(('student.urls', 'student'))),
    path('lecturer/', include(('lecturer.urls', 'lecturer'))),
    #url(r'^StudyPlan', include('student.urls'))
]
