from django.urls import path
from leaves import views

app_name ='leaves'

urlpatterns = [
    path('', views.leavestructure, name='leavestructure'),
    path('leavestructure/', views.leavestructure, name='leavestructure'),
    path('leavestructureajax/', views.leavestructureajax, name='leavestructureajax'),
    path('shortnameajax/', views.shortnameajax, name='shortnameajax'),
    path('editleavestructure/<int:id>/', views.editleavestructure, name='editleavestructure'),
    path('editleavestructureajax/<int:id>/', views.editleavestructureajax, name='editleavestructureajax'),
    path('editshortnameajax/<int:id>/', views.editshortnameajax, name='editshortnameajax'),
    path('leavetype/', views.leavetype, name='leavetype'),
    path('leavetypeajax/', views.leavetypeajax, name='leavetypeajax'),
    path('typeshortnameajax/', views.typeshortnameajax, name='typeshortnameajax'),
    path('assignleavestructure/', views.assignleavestructure, name='assignleavestructure'),
    path('editleavetype/<int:id>/', views.editleavetype, name='editleavetype'),
    path('editleavetypeajax/<int:id>/', views.editleavetypeajax, name='editleavetypeajax'),
    path('edittypeshortnameajax/<int:id>/', views.edittypeshortnameajax, name='edittypeshortnameajax'),
    path('relationwithleave/<int:id>/', views.relationwithleave, name='relationwithleave'),
    path('delete/<int:id>/<int:idleave>',views.delete,name='delete'),
    path('holidays/', views.holidays, name='holidays'),
    path('holidayajax/', views.holidayajax, name='holidayajax'),
    path('upload/', views.upload, name='upload'),
    path('applyleave/', views.applyleave, name='applyleave'),
    path('saveleaverequest/', views.saveleaverequest, name='saveleaverequest'),
    path('leaverequested/', views.leaverequested, name='leaverequested'),
    path('getleavedetails/', views.getleavedetails, name='getleavedetails'),
    path('cancelrequest/', views.cancelrequest, name='cancelrequest'),
]

