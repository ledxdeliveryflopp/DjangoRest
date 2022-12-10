from django.urls import path
from .views import AuthorsAPIView, AuthorDetail

app_name = 'author'

urlpatterns = [
    path('all/', AuthorsAPIView.as_view(), name='authors-all'),
    path('<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
]
