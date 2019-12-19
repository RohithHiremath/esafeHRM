from django.urls import path
from . import views


urlpatterns = [
    path('', views.jobtitles, name='jobtitle'),
    path('jobtitle/', views.jobtitles, name='jobtitle'),
    path('jobtitlesajax/', views.jobtitlesajax, name='jobtitlesajax'),
    path('editjobtitle/<int:id>/', views.editjobtitles, name='editjobtitle'),
    path('editjobtitlesajax/<int:id>/', views.editjobtitlesajax, name='editjobtitlesajax'),
    path('jobcategory/', views.jobcategories, name='jobcategory'),
    path('editjobcategory/<int:id>/', views.editjobcategories, name='editjobcategory'),
    path('jobgrade/', views.jobgrade, name = 'jobgrade'),
    path('jobgradeajax/', views.jobgradeajax, name = 'jobgradeajax'),
    path('editjobgrade/<int:id>/', views.editjobgrade, name='editjobgrade'),
    path('editjobgradeajax/<int:id>/', views.editjobgradeajax, name='editjobgradeajax'),
    path('component/', views.component, name = 'component'),
    path('editcomponent/<int:id>/', views.editcomponent, name='editcomponent'),
    path('status/', views.employementstatus, name = 'status'),
    path('employementstatusajax/', views.employementstatusajax, name = 'employementstatusajax'),
    path('editstatus/<int:id>/', views.editemployementstatus, name='editstatus'),
    path('editemployementstatusajax/<int:id>/', views.editemployementstatusajax, name='editemployementstatusajax'),
    path('department/', views.department, name = 'department'),
    path('departmentajax/', views.departmentajax, name = 'departmentajax'),
    path('editdepartment/<int:id>/', views.editdepartment, name='editdepartment'),
    path('editdepartmentajax/<int:id>/', views.editdepartmentajax, name='editdepartmentajax'),
    path('worklocation/', views.worklocation, name = 'worklocation'),
    path('locationajax/', views.locationajax, name = 'locationajax'),
    path('editlocation/<int:id>/', views.editlocation, name='editlocation'),
    path('editlocationajax/<int:id>/', views.editlocationajax, name='editlocationajax'),
]