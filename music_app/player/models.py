from django.db import models

# Create your models here.
from django.db import models

# Artist model
class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='artist_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# Album model
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='album_covers/', blank=True, null=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title

# Song model
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')  # 🔥 Fix here
    audio_file = models.FileField(upload_to='songs/')
    cover_image = models.ImageField(upload_to='song_covers/', blank=True, null=True)
    duration = models.DurationField()
    genre = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

# Playlist model
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
