from django.urls import path
from leaves import views

app_name ='leaves'

urlpatterns = [
    path('', views.leavestructure, name='leavestructure'),
    path('leavestructure/', views.leavestructure, name='leavestructure'),
    path('validateleavestructure/', views.validateleavestructure, name='validateleavestructure'),
    path('editleavestructure/<int:id>/', views.editleavestructure, name='editleavestructure'),
    path('validateeditleavestructure/<int:id>/', views.validateeditleavestructure, name='validateeditleavestructure'),
    path('leavetype/', views.leavetype, name='leavetype'),
    path('validateleavetype/', views.validateleavetype, name='validateleavetype'),
    path('assignleavestructure/', views.assignleavestructure, name='assignleavestructure'),
    path('editleavetype/<int:id>/', views.editleavetype, name='editleavetype'),
    path('editvalidateleavetype/<int:id>/', views.editvalidateleavetype, name='editvalidateleavetype'),
    path('relationwithleave/<int:id>/', views.relationwithleave, name='relationwithleave'),
    path('delete/<int:id>/<int:idleave>',views.delete,name='delete'),
]
