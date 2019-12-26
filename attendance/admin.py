from django.contrib import admin
from attendance.models import TardinessDetails,ShiftDetails,ShiftTimings
# # Register your models here.
admin.site.register(TardinessDetails) 
admin.site.register(ShiftDetails)
admin.site.register(ShiftTimings)