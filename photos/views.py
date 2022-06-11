from django.contrib.auth import authenticate, login as dj_login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Photo, Category
from .forms import CustomUserCreationForm


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            dj_login(request, user)
            return redirect('gallery')

    return render(request, 'photos/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                dj_login(request, user)
                return redirect('gallery')

    context = {'form': form, 'page': page}
    return render(request, 'photos/login_register.html', context)


@login_required(login_url='login')
def gallery(request):
    photos = Photo.objects.filter(category__user=request.user).order_by('-created_at')
    categories = Category.objects.filter(user=request.user).order_by('-id')

    category = request.GET.get('category_name')
    if category:
        photos = photos.filter(category__name=category)

    context = {
        'photos': photos,
        'categories': categories
    }
    return render(request, 'photos/gallery.html', context)


@login_required(login_url='login')
def view_photo(request, pk):
    photo = Photo.objects.get(pk=pk)

    context = {'photo': photo}
    return render(request, 'photos/photo.html', context)


@login_required(login_url='login')
def add_photo(request):
    categories = Category.objects.filter(user=request.user)

    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist('images')

        # print('data>>>', data)
        # print('images>>>', images)

        if data['category_new'] != '':  # if user created a new category
            category, create = Category.objects.get_or_create(name=data['category_new'],user=request.user)
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
