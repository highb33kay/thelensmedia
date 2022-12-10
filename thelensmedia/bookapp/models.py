from django.db import models
from vendor.models import Vendor
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

# create book model


class book(models.Model):

    # create a tuple of categories
    categories = (
        ('Poetry', 'Poetry'),
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Children', 'Children'),
        ('Education', 'Education'),
        ('Religion', 'Religion'),
        ('Self-Help', 'Self-Help'),
        ('Business', 'Business'),
        ('Cooking', 'Cooking'),
        ('Fantasy', 'Fantasy'),
        ('Young Adult', 'Young Adult'),
        ('Romance', 'Romance'),
        ('Mystery', 'Mystery'),
    )

    category = models.CharField(max_length=100, choices=categories)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='media/images/')
    slug = models.SlugField(max_length=100, unique=True)
    file = models.FileField(upload_to='media/files/')

    # auto populate slug with title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    # return the absolute url of the book
    def get_absolute_url(self):
        return reverse('bookapp,book_detail', args=[self.slug])

    # return the title of the book
    def __str__(self):
        return self.title

    # return the price of the book
    def get_price(self):
        return self.price
