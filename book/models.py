from django.db import models
from django.core.validators import FileExtensionValidator

from author.models import Author


# from core.models import Core


class Book(models.Model):
    """ Модель книги """
    title = models.CharField(max_length=100, verbose_name='Наименования', unique=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    year_of_rel = models.IntegerField(verbose_name='Год выпуска', default=2000)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, verbose_name='Издательство', blank=True,
                                  null=True)
    lang = models.ForeignKey('Languages', on_delete=models.CASCADE, verbose_name='Язык книги', blank=True, null=True)

    photoPreview = models.ImageField(upload_to='cover', verbose_name='Изображения', blank=True, null=True)
    book_file = models.FileField(upload_to='books', verbose_name='Файл с книгой', blank=True, null=True,
                                 validators=[FileExtensionValidator(allowed_extensions=['pdf',
                                                                                        'doc',
                                                                                        'docx',
                                                                                        'odt'])])

    class Meta:
        unique_together = ('title', 'author', 'year_of_rel')
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self) -> str:
        return f'{self.title}'


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименования', unique=True, null=True)
    """ Модель жанра """

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименования', unique=True, null=True)
    """ Модель категории """

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return f'{self.title}'


class Publisher(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименования', unique=True, null=True)
    """ Модель издательство """

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательство'

    def __str__(self) -> str:
        return f'{self.title}'


class Languages(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименования', unique=True, null=True)
    """ Модель языка """

    class Meta:
        verbose_name = 'Язык книги'
        verbose_name_plural = 'Язык книги'

    def __str__(self) -> str:
        return f'{self.title}'
