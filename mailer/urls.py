
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', Homepage.as_view(),name='Homepage'),
    path('listmail/', ListEmail.as_view(),name='ListEmail'),
    path('search_emails/', SearchEmails.as_view(), name='search_emails'),
] 
