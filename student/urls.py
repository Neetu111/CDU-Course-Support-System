from django.conf.urls import include, url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='student/index.html'),
    url(r'^StudyPlan.html', views.StudyPlan, name='student/StudyPlan.html'),
]