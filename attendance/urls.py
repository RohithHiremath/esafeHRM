from django.urls import path
from attendance import views

app_name ='attendance'

urlpatterns = [
    path('policies', views.policyDetails, name='policies'),
    path('shiftdetails', views.shiftDetails, name='shiftdetails'),
    path('validateshiftdetails', views.validateshiftDetails, name='validateshiftdetails'),
    path('shifttimings', views.ShiftTimings, name='shifttimings'),
    path('employeeshiftlist', views.employeeshiftlist, name='employeeshiftlist'),
]