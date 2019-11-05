from django.contrib import admin
from leaves.models import Leavestructure, Leavetype, Linktoleavetype
# Register your models here.

admin.site.register(Leavestructure)
admin.site.register(Leavetype)
admin.site.register(Linktoleavetype)