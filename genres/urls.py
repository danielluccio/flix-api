from django.urls import path
from .views import list_genres

urlpatterns = [
    path('', list_genres, name='list_genres'),
]