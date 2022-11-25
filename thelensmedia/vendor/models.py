from django.db import models
from django.contrib.auth.models import User
# import PIL
from PIL import Image
# import slugify
from django.template.defaultfilters import slugify
# import reverse
from django.urls import reverse
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
