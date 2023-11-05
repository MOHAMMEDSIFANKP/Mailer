
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', Homepage.as_view(),name='Homepage'),
] 
