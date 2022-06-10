from django.shortcuts import render, redirect
from .models import Photo, Category


def gallery(request):
    photos = Photo.objects.all().order_by('-created_at')
    categories = Category.objects.all().order_by('-id')

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
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist('images')

        # print('data>>>', data)
        # print('images>>>', images)

        if data['category_new'] != '':  # if user created a new category
            category, create = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = Category.objects.get(pk=data['category'])  # because {{data['category']}} is return category's id

        for image in images:
            photo = Photo.objects.create(
                category=category,
                title=data['title'],
                image=image,
            )
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add_photo.html', context)
