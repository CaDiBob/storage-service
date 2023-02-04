from django.contrib import admin

from storages.models import Part, Order, OrderItem


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
