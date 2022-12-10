from django.db import models
from django.core.validators import FileExtensionValidator

from author.models import Author
from core.models import Core


class Book(Core):
    """ Модель книги """
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    year_of_rel = models.DateField(verbose_name='Год выпуска')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр', blank=True)
    category = models.ManyToManyField('Category', verbose_name='Категория', blank=True)
    publisher = models.ManyToManyField('Publisher', verbose_name='Издательство', blank=True)

    # photoPreview = models.ImageField(validators=[validate_image], upload_to='cover',
    #                                   verbose_name='Изображения',
    #                                  blank=False, null=True)
    book_file = models.FileField(upload_to='books', verbose_name='Файл с книгой', blank=True,
                                 validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'odt'])])

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
