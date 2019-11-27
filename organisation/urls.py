from django.urls import path
from . import views

app_name ='organisation'

urlpatterns = [
    path('levels', views.addlevel, name='addlevel'),
    path('orgchart', views.orgchart, name='orgchart'),
    path('orgchartdata', views.orgchartdata, name='orgchartdata')
]