from django.urls import path
from .views import genre_create_list_view, genre_detail_view

urlpatterns = [
    path('', genre_create_list_view, name='list_genres'),
    path('<int:pk>', genre_detail_view, name='genre_detail_view')
]