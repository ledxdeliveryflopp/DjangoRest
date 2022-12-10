from rest_framework import generics, filters

from .models import Book
from .serializer import BooksSerializer


class BooksAPIView(generics.ListCreateAPIView):
    """ Вывод всех книг """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__first_name', 'genre']


class BookDetail(generics.RetrieveAPIView):
    """ Получить информацию о книге по ее id """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
