from django.contrib import admin
from payroll.models import Salarycomponent, PayScale, Linktocomponent, AssigningLevelsToPayscale
# Register your models here.

admin.site.register(Salarycomponent)
admin.site.register(PayScale)
admin.site.register(Linktocomponent)
admin.site.register(AssigningLevelsToPayscale)