from django.conf.urls import include, url
from .import views

app_name = 'student'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^StudyPlan.html', views.StudyPlan, name='StudyPlan'),
	url(r'^FinalStudyPlan.html', views.FinalStudyPlan, name='FinalStudyPlan'),
]