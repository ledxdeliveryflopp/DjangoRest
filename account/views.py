from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги', blank=False)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, max_length=100, verbose_name='Автор', blank=False)
    year_of_rel = models.IntegerField(verbose_name='Год выпуска', blank=False,
                                    validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    genre = models.CharField(max_length=100, verbose_name='Жанр', blank=True)
    #FIXME: сделать отдельную модель категорий, ForeignKey
    category = models.CharField(max_length=100, verbose_name='Категория', blank=True)
    publisher = models.CharField(max_length=100, verbose_name='Издательство', blank=True)

    # def validate_image(value):
    #     size_limit = 2 * 1024 * 1024
    #     if value.size > size_limit:
    #         raise forms.ValidationError('Файл слишком большой. Размер файла не должен превышать 2MB')

    # photoPreview = models.ImageField(validators=[validate_image], upload_to='cover',
    #                                   verbose_name='Изображения',
    #                                  blank=False, null=True)
    book_file = models.FileField(upload_to='books', verbose_name='Файл с книгой', blank=False,
                                null=True)

    class Meta:
        # unique_together = ('title', 'author', 'year_of_rel', 'publisher')
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
