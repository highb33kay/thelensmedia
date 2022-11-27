from django.contrib import admin
from .models import Vendor, Category, Product, Ticket
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name', 'bio', 'slug', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('vendor_name',)}


admin.site.register(Vendor, VendorAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('Category',), 'name': ('Category',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'vendor', 'Category', 'image',
                    'file', 'price', 'available', 'created', 'updated', 'slug']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Product, ProductAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_name', 'ticket_description', 'ticket_price', 'ticket_category', 'image',
                    'ticket_file', 'ticket_available', 'ticket_created',  'ticket_updated']
    prepopulated_fields = {'ticket_slug': (
        'ticket_name',)}


admin.site.register(Ticket, TicketAdmin)
