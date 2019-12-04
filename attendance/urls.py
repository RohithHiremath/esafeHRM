from django.urls import path
from attendance import views

app_name ='attendance'

urlpatterns = [
    path('policies/', views.policyDetails, name='policies'),
    path('shiftdetails/', views.shiftDetails, name='shiftdetails'),
    path('uploadattendance/', views.uploadattendance, name='uploadattendance')
]