from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Book, Genre, Category


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BooksSerializer(ModelSerializer):
    """ """
    author = SerializerMethodField(method_name='get_author')
    genre = GenreSerializer(many=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'year_of_rel', 'genre', 'category', 'publisher', 'author']

    @staticmethod
    def get_author(obj) -> str:
        return f'{obj.author.first_name} ' \
               f'{obj.author.last_name}'
