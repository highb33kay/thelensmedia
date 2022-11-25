from django.contrib import admin
from .models import Vendor
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name', 'bio', 'slug', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('vendor_name',)}


admin.site.register(Vendor, VendorAdmin)
