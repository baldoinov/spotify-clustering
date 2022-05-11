import spotipy
import csv
import boto3
from datetime import datetime

from config_playlist import spotify_playlist

spotipy_object = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

final_data_dictionary = {'Year Released': [],
                         'Album Lenght': [],
                         'Album Name': [],
                         'Artist': []
}

PLAYLIST = 'trapando'

def gather_data_local():

    with open:
        pass