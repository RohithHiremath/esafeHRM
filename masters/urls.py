from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobtitles, name='jobtitle'),
    path('jobtitle/', views.jobtitles, name='jobtitle'),
    path('<int:id>/', views.editjobtitles, name='editjobtitle'),
    path('jobcategories/', views.jobcategories, name='jobcategories'),
    path('jobgrades/', views.jobgrades, name = 'jobgrades')
]