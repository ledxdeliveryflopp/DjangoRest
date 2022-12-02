# Generated by Django 3.2.16 on 2022-12-02 14:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название книги')),
                ('year_of_rel', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)], verbose_name='Год выпуска')),
                ('genre', models.CharField(blank=True, max_length=100, verbose_name='Жанр')),
                ('category', models.CharField(blank=True, max_length=100, verbose_name='Категория')),
                ('publisher', models.CharField(blank=True, max_length=100, verbose_name='Издательство')),
                ('book_file', models.FileField(null=True, upload_to='books', verbose_name='Файл с книгой')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]