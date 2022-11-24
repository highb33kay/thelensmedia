from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse
from django.template.defaultfilters import slugify

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
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def str(self):
        return self.user.username


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
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vendor_name = models.CharField(max_length=255)
    bio = models.TextField()
    logo = models.ImageField(upload_to='vendor_logo')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.vendor_name

    def get_absolute_url(self):
        return reverse('vendor_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.vendor_name)
        return super().save(*args, **kwargs)
