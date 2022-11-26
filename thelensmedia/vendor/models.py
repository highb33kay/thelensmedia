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


# transferable digital product model
class Product(models.Model):

    # generate a unique id for each product
    product_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='Media/product_images/vendor')
    file = models.FileField(upload_to='Media/product_files/vendor', )
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.name


# product category model
class Category(models.Model):
    categories = (
        ('Music', 'Music'),
        ('Video', 'Video'),
        ('Software', 'Software'),
        ('Ebook', 'Ebook'),
        ('manuscript', 'Manuscript'),
        ('image', 'Image'),
        ('socials', 'Socials'),
    )

    Category = models.CharField(max_length=100, choices=categories)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
