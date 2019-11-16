from django.urls import path
from payroll import views

app_name ='payroll'

urlpatterns =[
    path('salaryheads/',views.salaryheadlist, name = 'salaryheads'),
    path('editsalaryhead/<int:id>/', views.editsalaryhead, name='editsalaryhead'),
    path('payscale/',views.payscalelist, name = 'payscale'),
    path('editpayscale/',views.editpayscale, name = 'editpayscale'),
    path('payscaleheads',views.linkpayscalehead,name='payscaleheads')
]