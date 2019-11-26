from django.urls import path
from pim import views

app_name ='pim'

urlpatterns =[
    path('employeelist/',views.employeelist, name = 'employeelist'),
    path('details/',views.Personal_details_view, name = 'details'),
    path('update/<int:id>/',views.update,name='update'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('getdropdownvalues/',views.getdropdownvalues,name='getdropdownvalues'),
    path('getmanagers/',views.getmanagers,name='getmanagers')
]