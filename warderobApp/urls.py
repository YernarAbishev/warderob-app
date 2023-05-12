from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('looks/view/', views.looksPage, name='looksPage'),
    path('looks/filter/age/<slug:slug>/', views.filterByAge, name='filterByAge'),
    path('looks/filter/season/<slug:slug>/', views.filterBySeason, name='filterBySeason'),
    path('looks/filter/weather/<slug:slug>/', views.filterByWeather, name='filterByWeather'),
    path('looks/filter/style/<slug:slug>/', views.filterByStyle, name='filterByStyle'),
    path('look/detail/<int:pk>/', views.lookDetailPage, name='lookDetailPage'),
    path('user/sign-up/', views.signUp, name='signUp'),
    path('user/login/', views.loginPage, name='loginPage'),
    path('user/logout/', views.logoutUser, name='logoutUser'),
    path('user/profile/', views.userProfilePage, name='userProfilePage'),
    path('user/favorites/', views.userFavoritesPage, name='userFavoritesPage'),
    path('favorite/<int:pk>/', views.toggle_favorite, name='toggle_favorite'),
    path('unfavorite/<int:pk>/', views.toggle_unfavorite, name='toggle_unfavorite'),
    path('user/change-password/',
         auth_views.PasswordChangeView.as_view(template_name='change-password.html', success_url='/'),
         name='change_password'),

]