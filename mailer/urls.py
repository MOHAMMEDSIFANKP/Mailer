
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', Homepage.as_view(),name='Homepage'),
    path('listmail/', ListEmail.as_view(),name='ListEmail'),
] 
