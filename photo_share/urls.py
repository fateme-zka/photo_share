from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photos.urls')),
]

# Just to show our images and medias in our project url (in the browser)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# To look into our static files in url
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
