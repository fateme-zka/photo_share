from django.shortcuts import render


def gallery(request):
    return render(request, 'photos/gallery.html', {})


def view_photo(request):
    return render(request, 'photos/photo.html', {})


def add_photo(request):
    return render(request, 'photos/add_photo.html', {})
