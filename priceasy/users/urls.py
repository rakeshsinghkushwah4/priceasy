from django.urls import path, include
from users import views

urlpatterns = [
    path('register/', views.Register, name="register"),
]
