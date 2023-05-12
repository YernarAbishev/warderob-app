from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import *
from .forms import *

#
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required



# басты бет
def homePage(request):
    looks = Look.objects.all()[:3]
    return render(request, 'home.html', {
        'looks': looks
    })


def looksPage(request):
    ages = Age.objects.all()
    weathers = Weather.objects.all()
    seasons = Season.objects.all()
    styles = Style.objects.all()
    looks = Look.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        looks = Look.objects.filter(Q(lookName__icontains=searchData) | Q(description__icontains=searchData))
    else:
        looks = Look.objects.all()
    return render(request, 'looks.html', {
        'ages': ages,
        'weathers': weathers,
        'seasons': seasons,
        'styles': styles,
        'looks': looks
    })

def filterByAge(request, slug=None):
    age = None
    ages = Age.objects.all()
    weathers = Weather.objects.all()
    seasons = Season.objects.all()
    styles = Style.objects.all()
    looks = Look.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        looks = Look.objects.filter(Q(lookName__icontains=searchData) | Q(description__icontains=searchData))
    else:
        looks = Look.objects.all()
    if slug:
        age = get_object_or_404(Age, slug=slug)
        looks = looks.filter(age=age)

    return render(request, 'looks-by-age.html', {
        'age': age,
        'ages': ages,
        'weathers': weathers,
        'seasons': seasons,
        'styles': styles,
        'looks': looks
    })

def filterByWeather(request, slug=None):
    weather = None
    ages = Age.objects.all()
    weathers = Weather.objects.all()
    seasons = Season.objects.all()
    styles = Style.objects.all()
    looks = Look.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        looks = Look.objects.filter(Q(lookName__icontains=searchData) | Q(description__icontains=searchData))
    else:
        looks = Look.objects.all()
    if slug:
        weather = get_object_or_404(Weather, slug=slug)
        looks = looks.filter(weather=weather)

    return render(request, 'looks-by-weather.html', {
        'weather': weather,
        'ages': ages,
        'weathers': weathers,
        'seasons': seasons,
        'styles': styles,
        'looks': looks
    })

def filterBySeason(request, slug=None):
    season = None
    ages = Age.objects.all()
    weathers = Weather.objects.all()
    seasons = Season.objects.all()
    styles = Style.objects.all()
    looks = Look.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        looks = Look.objects.filter(Q(lookName__icontains=searchData) | Q(description__icontains=searchData))
    else:
        looks = Look.objects.all()
    if slug:
        season = get_object_or_404(Season, slug=slug)
        looks = looks.filter(season=season)

    return render(request, 'looks-by-season.html', {
        'season': season,
        'ages': ages,
        'weathers': weathers,
        'seasons': seasons,
        'styles': styles,
        'looks': looks
    })

def filterByStyle(request, slug=None):
    style = None
    ages = Age.objects.all()
    weathers = Weather.objects.all()
    seasons = Season.objects.all()
    styles = Style.objects.all()
    looks = Look.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        looks = Look.objects.filter(Q(lookName__icontains=searchData) | Q(description__icontains=searchData))
    else:
        looks = Look.objects.all()
    if slug:
        style = get_object_or_404(Style, slug=slug)
        looks = looks.filter(style=style)

    return render(request, 'looks-by-style.html', {
        'style': style,
        'ages': ages,
        'weathers': weathers,
        'seasons': seasons,
        'styles': styles,
        'looks': looks
    })


def lookDetailPage(request, pk):
    look = get_object_or_404(Look, pk=pk)
    return render(request, 'look-detail.html', {
        'look': look
    })

def userProfilePage(request):
    return render(request, 'profile.html')

def toggle_favorite(request, pk):
    look = get_object_or_404(Look, pk=pk)
    try:
        favorite = Favorite.objects.get(user=request.user, look=look)
        favorite.delete()
        favorited = False
    except Favorite.DoesNotExist:
        favorite = Favorite.objects.create(user=request.user, look=look)
        favorited = True
    data = {'favorited': favorited, 'favorite_count': look.favorite_set.count()}
    return redirect("looksPage")

def toggle_unfavorite(request, pk):
    look = get_object_or_404(Look, pk=pk)
    try:
        favorite = Favorite.objects.get(user=request.user, look=look)
        favorite.delete()
        favorited = False
    except Favorite.DoesNotExist:
        favorite = Favorite.objects.create(user=request.user, look=look)
        favorited = True
    data = {'favorited': favorited, 'favorite_count': look.favorite_set.count()}
    return redirect("userFavoritesPage")

def userFavoritesPage(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)

    return render(request, 'user-favorites.html', {
        'favorites': favorites
    })

def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Тіркелу сәтті өтті!")
            return redirect("homePage")
        messages.error(request, "Тіркелу барысында қателіктер пайда болды")
    else:
        form = NewUserForm()
    return render(request, "sign-up.html", {
        'form': form
    })

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Қош келдіңіз, {username}!")
                return redirect("homePage")
            else:
                messages.error(request, "Логин немесе пароль қате.")
        else:
            messages.error(request, "Логин немесе пароль қате.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    messages.info(request, "Сіз платформадан сәтті шықтыңыз.")
    return redirect("homePage")