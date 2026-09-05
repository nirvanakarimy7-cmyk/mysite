from django.contrib import admin
from . import models
from django.contrib.auth.models import User

admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.Profile)

class profileinline(admin.StackedInline):
    model = models.Profile

class useradmin(admin.ModelAdmin):
    model = User
    fields=['username','first_name','last_name','email']
    inlines=[profileinline]

admin.site.unregister(User)
admin.site.register(User,useradmin)