from django.urls import path
from .views import *

urlpatterns = [
    path('', gallery, name='gallery'),
    path('photo/', view_photo, name='photo'),
    path('add_photo/', add_photo, name='add-photo'),

]
