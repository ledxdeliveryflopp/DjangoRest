from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Book


class BooksSerializer(ModelSerializer):
    """ """
    author = SerializerMethodField(method_name='get_author')

    class Meta:
        model = Book
        fields = ['id', 'title', 'year_of_rel', 'genre', 'publisher', 'author']

    @staticmethod
    def get_author(obj) -> str:
        return f'{obj.author.first_name} ' \
               f'{obj.author.middle_name}' \
               f'{obj.author.last_name}'
