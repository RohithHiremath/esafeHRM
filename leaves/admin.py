from django.contrib import admin
from leaves.models import Holidays, Leavestructure, Leavetype, Linktoleavetype, AssignLeaveStructure
# Register your models here.

admin.site.register(Leavestructure)
admin.site.register(Leavetype)
admin.site.register(Linktoleavetype)
admin.site.register(AssignLeaveStructure)
admin.site.register(Holidays)