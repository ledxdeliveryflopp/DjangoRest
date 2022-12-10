from django.db import models


class Author(models.Model):
    """ Модель автора книги """
    first_name = models.CharField(max_length=100, verbose_name='Имя', blank=False)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', blank=True)
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', blank=False)
    date_of_birth = models.DateField(max_length=100, verbose_name='Дата рождения', blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.middle_name}'

    class Meta:
        unique_together = ('first_name', 'last_name', 'middle_name', 'date_of_birth')
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
