from django.urls import path
from .views import ListAnimes, CreateAnime, UpdateAnime, DeleteAnime

urlpatterns = [
    path('', ListAnimes.as_view(), name='list_animes'),
    path('create_anime/', CreateAnime.as_view(), name='create_anime'),
    path('update_anime/<int:pk>', UpdateAnime.as_view(), name='update_anime'),
    path('delete_anime/<int:pk>', DeleteAnime.as_view(), name='delete_anime')
]