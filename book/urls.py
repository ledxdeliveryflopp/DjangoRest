from django.urls import path
from .views import BooksAPIView, BookDetail, BookCreate

app_name = 'book'

urlpatterns = [
    path('all/', BooksAPIView.as_view(), name='books-all'),
    path('<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('create/', BookCreate.as_view(), name='book-create'),
]
