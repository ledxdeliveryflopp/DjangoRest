from rest_framework import generics

from .models import Author
from .serializer import BooksSerializer


class AuthorsAPIView(generics.ListCreateAPIView):
    """ Вывод всех авторов """
    queryset = Author.objects.all()
    serializer_class = BooksSerializer


class AuthorDetail(generics.RetrieveAPIView):
    """ Получить информацию о авторе по его id """
    queryset = Author.objects.all()
    serializer_class = BooksSerializer
