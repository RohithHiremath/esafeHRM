from django.urls import path
from empprofile import views

app_name ='empprofile'

urlpatterns = [
    path('myprofile/', views.profiledetails, name='profiledetails'),
    path('proupdate/<int:id>/', views.editprofile, name='proupdate'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('checkoldpassword/', views.checkoldpassword, name='checkoldpassword'),
]

