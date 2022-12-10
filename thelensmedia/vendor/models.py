from django.db import models
from django.contrib.auth.models import User
# import PIL
from PIL import Image
# import slugify
from django.template.defaultfilters import slugify
# import reverse
from django.urls import reverse
# import uuid
import uuid
from uuid import uuid4

# Create your models here.


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=100)
    bio = models.TextField()
    logo = models.ImageField(upload_to='Media/vendor_logo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ['vendor_name']

    def __str__(self):
        return self.vendor_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.logo.path)

    def get_absolute_url(self):
        return reverse('vendor_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.vendor_name)
        return super().save(*args, **kwargs)

# product category model


# class Category(models.Model):
#     categories = (
#         ('Music', 'Music'),
#         ('Video', 'Video'),
#         ('Software', 'Software'),
#         ('Ebook', 'Ebook'),
#         ('manuscript', 'Manuscript'),
#         ('image', 'Image'),
#         ('socials', 'Socials'),
#         ('ticket', 'Ticket'),
#     )

#     Category = models.CharField(max_length=100, choices=categories)
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, unique=True)

#     # auto populate the name field with category name

#     class Meta:
#         verbose_name_plural = 'Categories'
#         ordering = ('Category',)

#     def get_absolute_url(self):
#         return reverse('store:product_list_by_category', args=[self.slug])

#     def __str__(self):
#         return self.Category

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         return super().save(*args, **kwargs)

# define the product owner model


# class ProductOwner(models.Model):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     product = models.ForeignKey(product, )

#     class Meta:
#         verbose_name_plural = 'Product Owners'
#         ordering = ('vendor',)

#     def __str__(self):
#         return self.vendor.vendor_name

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)


# transferable digital product model


# Ticket model that extends the product model
# class Ticket(Product):
#     ticket_id = models.UUIDField(
#         primary_key=True, default=uuid.uuid4, editable=False)
#     ticket_name = models.CharField(max_length=100)
#     ticket_description = models.TextField()
#     ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
#     ticket_category = models.ForeignKey(Category, on_delete=models.PROTECT)
#     ticket_image = models.ImageField(upload_to='Media/ticket_images/vendor')
#     ticket_file = models.FileField(upload_to='Media/ticket_files/vendor')
#     ticket_available = models.BooleanField(default=True)
#     ticket_created = models.DateTimeField(auto_now_add=True)
#     ticket_updated = models.DateTimeField(auto_now=True)
#     ticket_slug = models.SlugField(max_length=255)

#     # generate ticket qr code

#     def generate_qr_code(self):
#         qr = qrcode.QRCode(
#             version=1,
#             box_size=10,
#             border=5
#         )
#         data = f"{self.ticket_id}"
#         qr.add_data(data)
#         qr.make(fit=True)
#         img = qr.make_image(fill='black', back_color='white')
#         img.save(f"Media/ticket_qr_codes/{self.ticket_id}.png")

#     class Meta:
#         verbose_name_plural = 'Tickets'
#         ordering = ('-ticket_created',)

#     def get_absolute_url(self):
#         return reverse('store:ticket_detail', args=[self.ticket_slug])

#     def __str__(self):
#         return self.ticket_name

#     def save(self, *args, **kwargs):
#         if not self.ticket_slug:
#             self.ticket_slug = slugify(self.ticket_name)
#         return super().save(*args, **kwargs)

# # Disable fields if category is not tickets
# class Moses(models.Model):
#     pass
