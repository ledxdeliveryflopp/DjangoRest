from django.contrib import admin

from .models import Book, Genre, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class BookAdmin(admin.ModelAdmin):
    pass
