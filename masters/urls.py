from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobtitles, name='jobtitle'),
    path('jobtitle/', views.jobtitles, name='jobtitle'),
    path('editjobtitle/<int:id>/', views.editjobtitles, name='editjobtitle'),
    path('jobcategory/', views.jobcategories, name='jobcategory'),
    path('editjobcategory/<int:id>/', views.editjobcategories, name='editjobcategory'),
    path('jobgrade/', views.jobgrade, name = 'jobgrade'),
    path('editjobgrade/<int:id>/', views.editjobgrade, name='editjobgrade'),
    path('component/', views.component, name = 'component'),
    path('editcomponent/<int:id>/', views.editcomponent, name='editcomponent'),
    path('status/', views.employementstatus, name = 'status'),
    path('editstatus/<int:id>/', views.editemployementstatus, name='editstatus'),
    path('department/', views.department, name = 'department'),
    path('editdepartment/<int:id>/', views.editdepartment, name='editdepartment'),
]