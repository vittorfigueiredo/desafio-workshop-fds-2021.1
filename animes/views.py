from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Animes
from .forms import AnimeForm

# view para listar os Animes
class ListAnimes(ListView):
    model = Animes
    template_name = 'animes/list_animes.html'
    context_object_name = 'animes'

# view para adcionar um novo anime
class CreateAnime(CreateView):
    model = Animes
    template_name = 'animes/create_anime.html'
    form_class = AnimeForm
    success_url = reverse_lazy('list_animes')

# view para editar um anime existente
class UpdateAnime(UpdateView):
    model = Animes
    template_name = 'animes/update_anime.html'
    form_class = AnimeForm
    success_url = reverse_lazy('list_animes')

# view para deletar um anime
class DeleteAnime(DeleteView):
    model = Animes
    success_url = reverse_lazy('list_animes')