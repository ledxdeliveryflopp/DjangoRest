from rest_framework import generics, filters, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializer import BooksSerializer


class BooksAPIView(generics.ListCreateAPIView):
    """ Вывод всех книг """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__first_name', 'genre__title']
    # permission_classes = [IsAuthenticated]


class BookDetail(generics.RetrieveAPIView):
    """ Получить информацию о книге по ее id """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookCreate(generics.CreateAPIView):
    """ Получить информацию о книге по ее id """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
