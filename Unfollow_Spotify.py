import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# Configure suas credenciais
CLIENT_ID = 'token'
CLIENT_SECRET = 'token'
REDIRECT_URI = 'http://localhost:8888/callback'

# Configuração do OAuth
scope = 'user-follow-modify playlist-modify-public playlist-modify-private user-library-read user-follow-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

def unfollow_artists():
    # Pega os IDs dos artistas seguidos
    results = sp.current_user_followed_artists(limit=50)
    while results['artists']['items']:
        artist_ids = [artist['id'] for artist in results['artists']['items']]
        # Deixa de seguir os artistas
        sp.user_unfollow_artists(artist_ids)
        print(f"Deixou de seguir {len(artist_ids)} artistas.")
        time.sleep(1)  # Pausa de 1 segundo entre cada chamada
        results = sp.current_user_followed_artists(limit=50)

def unfollow_playlists():
    # Pega as playlists do usuário
    playlists = sp.current_user_playlists(limit=50)
    while playlists['items']:
        for playlist in playlists['items']:
            sp.current_user_unfollow_playlist(playlist['id'])
            print(f"Deixou de seguir a playlist: {playlist['name']}")
            time.sleep(1)  # Pausa de 1 segundo entre cada chamada
        playlists = sp.current_user_playlists(limit=50)

# Execute as funções
unfollow_artists()
unfollow_playlists()