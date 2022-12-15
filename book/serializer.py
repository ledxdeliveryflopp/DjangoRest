from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Book, Genre, Category, Publisher, Languages


class BooksSerializer(ModelSerializer):
    """ """

    class Meta:
        model = Book
        fields = ['id', 'title', 'year_of_rel', 'genre', 'category', 'publisher',
                  'lang', 'author', 'book_file', 'photoPreview']

