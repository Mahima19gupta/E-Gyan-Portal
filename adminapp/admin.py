from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Program)
admin.site.register(models.Branch)
admin.site.register(models.Year)
admin.site.register(models.Material)
admin.site.register(models.Events)
admin.site.register(models.Course)
admin.site.register(models.Question)
admin.site.register(models.Result)
