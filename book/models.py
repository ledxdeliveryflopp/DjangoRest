from django.db import models

from author.models import Author


class Book(models.Model):
    """ Модель книги """
    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, max_length=100, verbose_name='Автор')
    year_of_rel = models.DateField(verbose_name='Год выпуска')
    genre = models.CharField(max_length=100, verbose_name='Жанр', blank=True)
    # FIXME: сделать отдельную модель категорий, ForeignKey
    # category = models.CharField(max_length=100, verbose_name='Категория', blank=True)
    publisher = models.CharField(max_length=100, verbose_name='Издательство', blank=True)

    # def validate_image(value):
    #     size_limit = 2 * 1024 * 1024
    #     if value.size > size_limit:
    #         raise forms.ValidationError('Файл слишком большой. Размер файла не должен превышать 2MB')

    # photoPreview = models.ImageField(validators=[validate_image], upload_to='cover',
    #                                   verbose_name='Изображения',
    #                                  blank=False, null=True)
    book_file = models.FileField(upload_to='books', verbose_name='Файл с книгой', blank=True)

    class Meta:
        unique_together = ('title', 'author', 'year_of_rel', 'publisher')
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self) -> str:
        return f'{self.title}'
