from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'lecturer'

urlpatterns = [
    path('', views.lecturer_login, name='lecturer_login'),
    path('logout/', views.lecturer_logout, name='lecturer_logout'),
    path('<lecturer_name>', views.upload_page, name='upload_page'),
    path('<lecturer_name>/student_progress_report', views.show_student_progress_report, name='show_student_progress_report'),
    ]