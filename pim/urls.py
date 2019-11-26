from django.urls import path
from pim import views

app_name ='pim'

urlpatterns =[
    path('employeelist/',views.employeelist, name = 'employeelist'),
    path('details/',views.Personal_details_view, name = 'details'),
    path('email/',views.sendemail, name = 'email'),
    path('update/<int:id>/',views.update,name='update'),
    path('edit/<int:id>/',views.edit,name='edit'),
]