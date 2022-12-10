from django.db import models


class Author(models.Model):
    """ Модель автора книги """
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', blank=True)
    date_of_birth = models.DateField(max_length=100, verbose_name='Дата рождения')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.middle_name}'

    class Meta:
        unique_together = ('first_name', 'last_name', 'middle_name', 'date_of_birth')
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
