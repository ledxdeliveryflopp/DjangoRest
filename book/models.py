from django.db import models
from django.core.validators import FileExtensionValidator

from author.models import Author
from core.models import Core


class Book(Core):
    """ Модель книги """
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    year_of_rel = models.DateField(verbose_name='Год выпуска')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE ,verbose_name='Жанр', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, verbose_name='Издательство', blank=True)
    lang = models.ForeignKey('Languages', on_delete=models.CASCADE, verbose_name='Язык книги', blank=True)

    photoPreview = models.ImageField(upload_to='cover', verbose_name='Изображения', blank=True)
    book_file = models.FileField(upload_to='books', verbose_name='Файл с книгой', blank=True,
                                 validators=[FileExtensionValidator(allowed_extensions=['pdf',
                                                                                        'doc',
                                                                                        'docx',
                                                                                        'odt'])])

    class Meta:
        unique_together = ('title', 'author', 'year_of_rel')
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Genre(Core):
    """ Модель жанра """
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(Core):
    """ Модель категории """
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Publisher(Core):
    """ Модель издательство """
    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательство'


class Languages(Core):
    """ Модель языка """
    class Meta:
        verbose_name = 'Язык книги'
        verbose_name_plural = 'Язык книги'
