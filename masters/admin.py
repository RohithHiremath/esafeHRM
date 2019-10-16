from django.contrib import admin
from masters.models import Job,Jobcategory,Jobgrade,Salarycomponent,Employmentstatus,Department,Location
# Register your models here.
admin.site.register(Job)
admin.site.register(Jobcategory)
admin.site.register(Jobgrade)
admin.site.register(Salarycomponent)
admin.site.register(Employmentstatus)
admin.site.register(Department)
admin.site.register(Location)