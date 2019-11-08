from django.urls import path
from leaves import views

app_name ='leaves'

urlpatterns = [
    path('', views.leavestructure, name='leavestructure'),
    path('leavestructure/', views.leavestructure, name='leavestructure'),
    path('editleavestructure/<int:id>/', views.editleavestructure, name='editleavestructure'),
    path('leavetype/', views.leavetype, name='leavetype'),
    path('assignleavestructure/', views.assignleavestructure, name='assignleavestructure'),
    path('editleavetype/<int:id>/', views.editleavetype, name='editleavetype'),
    path('relationwithleave/<int:id>/', views.relationwithleave, name='relationwithleave'),
    path('delete/<int:id>/<int:idleave>',views.delete,name='delete'),
]
