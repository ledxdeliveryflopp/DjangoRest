from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Book
from .serializer import BooksSerializer


class BooksAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(genre='ужас')
    serializer_class = BooksSerializer
    permission_classes = [AllowAny]

    # def get_queryset(self):
    #     return Book.objects.all()


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
