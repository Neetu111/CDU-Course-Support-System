from django.conf.urls import include, url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='lecturer/lecturerlogin.html'),
    url(r'^uploadpage.html', views.UploadPage, name='lecturer/uploadpage.html'),
    ]