from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home')
]

#now connect this urls.py to main project urls.py