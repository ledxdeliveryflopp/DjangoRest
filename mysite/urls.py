from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/book/', include('book.urls', namespace='book')),
    path('api/v1/author/', include('author.urls', namespace='author')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
