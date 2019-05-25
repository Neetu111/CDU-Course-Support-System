from django.urls import path, re_path
from .import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('<course_field>-<course_code>-<semester>-<year>/', views.study_plan, name='study_plan'),
    path('<course_field>-<course_code>-<semester>-<year>/core_unit/', views.core_unit, name='core_unit'),
    path('<course_field>-<course_code>-<semester>-<year>/common_unit/', views.common_unit, name='common_unit'),
    path('<course_field>-<course_code>-<semester>-<year>/specialist_elective/', views.specialist_elective, name='specialist_elective'),
    path('<course_field>-<course_code>-<semester>-<year>/research_unit/', views.research_unit, name='research_unit'),
    path('<course_field>-<course_code>-<semester>-<year>/pre_requisite/', views.check_prerequisite, name='check_prerequisite'),
    path('<course_field>-<course_code>-<semester>-<year>/unit_deleted/', views.delete_unit, name='delete_unit'),
    path('<course_field>-<course_code>-<semester>-<year>/pre_requisite/final_study_plan/', views.final_study_plan, name='final_study_plan'),
]