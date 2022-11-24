from django.contrib import admin
from models import CustomerProfile, VendorProfile

# Register your models here.

# Register customer profile


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fname', 'lname', 'email')


admin.site.register(CustomerProfile, CustomerProfileAdmin)

# register vendor profile


class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fname', 'lname', 'email', 'vendor_name',
                    'bio', 'logo', 'created_at', 'updated_at', 'url')

    prepopulated_fields = {'slug': ('vendor_name',)}


admin.register(VendorProfile, VendorProfileAdmin)
