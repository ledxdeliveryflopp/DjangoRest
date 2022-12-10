from django.db import models


class Core(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименования', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        abstract = True
