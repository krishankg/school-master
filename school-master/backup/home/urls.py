from django.contrib import admin
from django.urls import path
from .views import HomeView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(),name='view'),
]