from django.urls import path, re_path
from .import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('<course_field>-<course_code>/', views.study_plan, name='study_plan'),
    path('<course_field>-<course_code>/pre_requisite/', views.check_prerequisite, name='check_prerequisite'),
    path('<course_field>-<course_code>/pre_requisite/final_study_plan/', views.final_study_plan, name='final_study_plan'),
]