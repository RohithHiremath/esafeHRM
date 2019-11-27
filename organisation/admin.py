from django.contrib import admin
from organisation.models import Leveldefinition, LevelDesignation, LevelGrades
# Register your models here.
admin.site.register(Leveldefinition)
admin.site.register(LevelDesignation)
admin.site.register(LevelGrades)
