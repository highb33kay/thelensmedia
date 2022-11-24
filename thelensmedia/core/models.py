from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create AbstractUser model


class User(AbstractUser):
    # define user roles database fields
    class Role(models.TextChoices):
        ADMIN = 'admin'
        Vendor = 'vendor'
        Customer = 'customer'

    # define base role
    base_role = Role.ADMIN

    # save the role of the user
    role = models.CharField(max_length=50, choices=Role.choices)

    # set default role to a user when they signup
    def save(self, *args, **kwargs):
        # if the user is not created
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

# Create Customer Model Manager


class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)

# register the a customer model


class Customer(User):
    base_role = User.Role.Customer

    customer = CustomerManager()

    class Meta:
        proxy = True

# customer profile model


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Customer = CustomerManager()


# Vendor Model Manager


class VendorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.VENDOR)

# register the vendor model


class Vendor(User):
    base_role = User.Role.VENDOR

    vendor = VendorManager()

    class Meta:
        proxy = True

# vendor profile model


class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Vendor = VendorManager()
