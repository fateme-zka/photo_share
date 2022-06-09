from django.shortcuts import render
from .models import Photo, Category


def gallery(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()

    context = {
        'photos': photos,
        'categories': categories
    }
    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk):
    photo = Photo.objects.get(pk=pk)

    context = {'photo': photo}
    return render(request, 'photos/photo.html', context)


def add_photo(request):
    return render(request, 'photos/add_photo.html', {})
