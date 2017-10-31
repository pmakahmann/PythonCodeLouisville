from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)


from . import models


def song_list(request):
    songs = models.Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})


#View for List of all Songs in Database
class SongListView(ListView):
    context_object_name = 'songs'
    model = models.Song

# Create Views for full CRUD capabilities

#View for Details of Song
class SongDetailView(DetailView):
    model = models.Song

#View for Adding Song
class SongCreateView(CreateView):
    fields = ('title', 'artist', 'composition_date')
    model = models.Song

#View for Updating Song Already in Database
class SongUpdateView(UpdateView):
    fields = ('title', 'artist', 'composition_date')
    model = models.Song

#View for Deleting a Song from the Database
#When successful, reverse_lazy returns user to ListView
class SongDeleteView(DeleteView):
    model = models.Song
    success_url = reverse_lazy("songs:list")
