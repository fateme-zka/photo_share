from django.urls import path
from .views import *

urlpatterns = [
    # user authentication
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),

    # gallery
    path('', gallery, name='gallery'),
    path('photo/<int:pk>/', view_photo, name='photo'),
    path('add_photo/', add_photo, name='add-photo'),

]
