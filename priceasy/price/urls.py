from django.urls import path

from price import views

urlpatterns = [
    path('home/', views.Home, name="home"),
]