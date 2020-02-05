from django.contrib import admin
from django.urls import path
from .views import PrincipalView

app_name = 'principal'
urlpatterns = [
    path('', PrincipalView.as_view(),name='view'),
]