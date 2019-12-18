from django.urls import path
from . import views

app_name ='organisation'

urlpatterns = [
    path('levels', views.addlevel, name='addlevel'),
    path('levelslist', views.levelslist, name='levelslist'),
    path('updatelist/<int:id>/', views.updatelist, name='updatelist'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('orgchart', views.orgchart, name='orgchart'),
    path('orgchartdata', views.orgchartdata, name='orgchartdata')
]