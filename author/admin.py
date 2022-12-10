from django.contrib import admin

from .models import Author


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    pass
