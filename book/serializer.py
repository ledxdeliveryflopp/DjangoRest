from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Book, Genre, Category, Publisher, Languages


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class LanguagesSerializer(ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class BooksSerializer(ModelSerializer):
    """ """
    author = SerializerMethodField(method_name='get_author')
    genre = GenreSerializer(many=True)
    category = CategorySerializer(many=True)
    publisher = PublisherSerializer(many=True)
    lang = LanguagesSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'year_of_rel', 'book_file', 'genre', 'category', 'publisher', 'lang', 'author']

    @staticmethod
    def get_author(obj) -> str:
        return f'{obj.author.first_name} ' \
               f'{obj.author.last_name}'
