from django.contrib import admin

from .models import book

# Register your models here.

# register the book model


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'slug',
                    'file', 'cover', 'created_at', 'updated_at']
    list_filter = ['title', 'created_at', 'updated_at', 'author']
    list_editable = ['price', 'file', 'cover']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(book, BookAdmin)
