from rest_framework import generics

from .models import Author
from .serializer import AuthorSerializer


class AuthorsAPIView(generics.ListCreateAPIView):
    """ Вывод всех авторов """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    """ Получить информацию о авторе по его id """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
