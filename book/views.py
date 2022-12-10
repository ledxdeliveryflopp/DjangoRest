from rest_framework import generics

from .models import Book
from .serializer import BooksSerializer


class BooksAPIView(generics.ListCreateAPIView):
    """ Вывод всех книг """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookDetail(generics.RetrieveAPIView):
    """ Получить информацию о книге по ее id """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
