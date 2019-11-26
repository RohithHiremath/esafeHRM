from django.urls import path
from pim import views

app_name ='pim'

urlpatterns =[
    path('employeelist/',views.employeelist, name = 'employeelist'),
    path('details/',views.Personal_details_view, name = 'details'),
    path('email/',views.sendemail, name = 'email'),
    path('update/<int:id>/',views.update,name='update'),
    path('edit/<int:id>/',views.edit,name='edit'),
<<<<<<< HEAD
=======
    path('getdropdownvalues/',views.getdropdownvalues,name='getdropdownvalues'),
    path('getmanagers/',views.getmanagers,name='getmanagers')
>>>>>>> 2b97f0d9dd5a3066a0ddb4c48d81d4d047367f7a
]