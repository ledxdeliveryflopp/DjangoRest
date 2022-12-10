from django.contrib import admin

from .models import Book, Genre, Category, Publisher, Languages


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    pass
