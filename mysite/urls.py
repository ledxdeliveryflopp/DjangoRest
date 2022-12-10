from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/v1/book/', include('book.urls', namespace='book')),
    path('api/v1/author/', include('author.urls', namespace='author')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
