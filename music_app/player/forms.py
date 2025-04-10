from django import forms
from .models import Song, Artist, Album

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            'title',
            'artist',
            'album',
            'audio_file',
            'cover_image',
            'duration',
            'genre'
        ]

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'image']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'cover_image', 'release_date']
