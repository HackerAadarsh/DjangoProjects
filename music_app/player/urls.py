from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('albums/', views.albums, name='albums'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
    path('artists/', views.artists, name='artists'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('upload_song/', views.upload_song, name='upload_song'),  # ✅ comma added here
    path('add_artist/', views.add_artist, name='add_artist'),
    path('add_album/', views.add_album, name='add_album'),
]
