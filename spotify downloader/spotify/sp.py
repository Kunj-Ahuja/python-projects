import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cId= 'a5f0636145e34e9abc809ba8b438cf6f'
cSecret = '139231d3247047209de6b9fa0898f4b3'

client_credentials_manager = SpotifyClientCredentials(client_id=cId, client_secret=cSecret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)