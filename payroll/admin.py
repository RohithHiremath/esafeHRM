from django.contrib import admin
from payroll.models import Salarycomponent, PayScale, Linktocomponent, AssigningLevelsToPayscale, AssignPayscale
# Register your models here.

admin.site.register(Salarycomponent)
admin.site.register(PayScale)
admin.site.register(Linktocomponent)
admin.site.register(AssigningLevelsToPayscale)
admin.site.register(AssignPayscale)