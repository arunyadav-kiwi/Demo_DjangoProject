from django.contrib import admin
from .models import BookData
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'auther_name', 'release_year', 'price']



admin.site.register(BookData, BookAdmin)