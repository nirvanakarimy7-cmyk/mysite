from django.contrib import admin
from.models import shippingdress,order,orderitem

admin.site.register(shippingdress)
admin.site.register(orderitem)

class OrderIteminline(admin.TabularInline):
    model=orderitem
    extra=0

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    readonly_fields=['date_ordered','last_update']
    inlines=[OrderIteminline]
