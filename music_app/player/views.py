from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Album, Artist
from .forms import SongForm, ArtistForm, AlbumForm

# Home Page - List of Songs
def home(request):
    songs = Song.objects.all().order_by('-id')[:9]
    return render(request, 'player/home.html', {'songs': songs})

# Song Detail Page
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'player/song_detail.html', {'song': song})

# Albums Page
def albums(request):
    albums = Album.objects.all()
    return render(request, 'player/albums.html', {'albums': albums})

# Album Detail Page
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = Song.objects.filter(album=album)
    return render(request, 'player/album_detail.html', {'album': album, 'songs': songs})

# Artists Page
def artists(request):
    artists = Artist.objects.all()
    return render(request, 'player/artists.html', {'artists': artists})

# Artist Detail Page
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    songs = Song.objects.filter(artist=artist)
    return render(request, 'player/artist_detail.html', {'artist': artist, 'songs': songs})

# Upload Song Page
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to home after upload
    else:
        form = SongForm()
    return render(request, 'player/upload_song.html', {'form': form})

# Add Artist Page
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artists')
    else:
        form = ArtistForm()
    return render(request, 'player/add_artist.html', {'form': form})

# Add Album Page
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums')
    else:
        form = AlbumForm()
    return render(request, 'player/add_album.html', {'form': form})
