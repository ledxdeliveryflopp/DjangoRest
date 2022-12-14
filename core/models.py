from django.db import models


class Core(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименования', unique=True)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        abstract = True
