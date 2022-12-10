from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('book/', include('book.urls', namespace='book')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
