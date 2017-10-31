from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

#Creation of only model in project.  Could be expanded later for more detail or
#could build new models and link with foreign keys.
class Song(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    #Included default values to keep from having 'Null' values
    artist = models.CharField(max_length=255, default="N/A")
    composition_date = models.PositiveIntegerField(default=1900)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('songs:detail', kwargs={'pk': self.pk})
