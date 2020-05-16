from django.contrib import admin
from . import models


admin.site.register(models.Person)
admin.site.register(models.Skill)
admin.site.register(models.Project)
admin.site.register(models.Experience)
admin.site.register(models.Skilltag)
admin.site.register(models.SocialMedia)