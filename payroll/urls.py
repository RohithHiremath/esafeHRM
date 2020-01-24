from django.urls import path
from payroll import views

app_name ='payroll'

urlpatterns =[
    path('component/', views.component, name = 'component'),
    path('componentajax/', views.componentajax, name = 'componentajax'),
    path('editcomponent/<int:id>/', views.editcomponent, name='editcomponent'),
    path('editcomponentajax/<int:id>/', views.editcomponentajax, name = 'editcomponentajax'),
    path('payscale/',views.payscalelist, name = 'payscale'),
    path('payscaleajax/', views.payscaleajax, name='payscaleajax'),
    path('payshortajax/', views.payshortajax, name='payshortajax'),
    path('assignpayscale/', views.assignpayscale, name = 'assignpayscale'),
    path('editpayscale/<int:id>/',views.editpayscale, name ='editpayscale'),
    path('editpayscaleajax/<int:id>/', views.editpayscaleajax, name='editpayscaleajax'),
    path('editpayshortajax/<int:id>/', views.editpayshortajax, name='editpayshortajax'),
    path('relationwithcomp/<int:id>/', views.relationwithcomp, name='relationwithcomp'),
    path('delete/<int:id>/<int:idpay>',views.delete,name='delete'),
]