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
    publisher = models.CharField(max_length=100, verbose_name='Издательство', blank=True)

    # photoPreview = models.ImageField(validators=[validate_image], upload_to='cover',
    #                                   verbose_name='Изображения',
    #                                  blank=False, null=True)
    book_file = models.FileField(upload_to='books', verbose_name='Файл с книгой', blank=True,
                                 validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'odt'])])

    class Meta:
        unique_together = ('title', 'author', 'year_of_rel', 'publisher')
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Genre(Core):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(Core):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
