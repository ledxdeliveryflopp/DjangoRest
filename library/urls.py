from django.urls import path
from .views import BooksAPIView, BookDetail

app_name = 'book'

urlpatterns = [
    path('all/', BooksAPIView.as_view(), name='books-all'),
    path('<int:pk>/', BookDetail.as_view(), name='book-detail'),
]