import spotipy

def get_artists_from_playlist(playlist_uri: str):
    '''
    :param playlist_uri: Playlist to analyse
    :return: A dict(artist uri: artist name) of all primary artists in a playlist
    '''

    credentials = spotipy.oauth2.SpotifyClientCredentials()
    spotify = spotipy.Spotify(client_credentials_manager=credentials)

    artists = {}
    playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_uri)

    for song in playlist_tracks['items']:
        
        if song['track']:
            # print(song['track']['artists'][0]['name'])
            artists[song['track']['artists'][0]['uri']] = song['track']['artists'][0]['name']
    
    return artists

if __name__ == '__main__':

    art = get_artists_from_playlist('spotify:playlist:0fBKZ2Bup5pjfFQaLLeQfc')
    print(art)