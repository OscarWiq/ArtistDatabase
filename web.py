import requests
import time

param_artist = "artist"
param_artists = "artists"
param_name = "name"
param_id = "id"

base_url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com"

cached_artists = []
cache_duration = 20  # cache lifetime in seconds
time_of_cache = -1  # time when cache was last updated


def fetch_artists():
    global time_of_cache, cache_duration, cached_artists
    url = base_url + '/artists/'
    if len(cached_artists) != 0 and time.time() - time_of_cache < cache_duration:
        return cached_artists
    else:
        api_artists = requests.get(url).json()[param_artists]
        cached_artists.clear()
        for artist in api_artists:
            cached_artists.append(artist)
        time_of_cache = time.time()
        return cached_artists


def fetch_artist(artist_id=-1):
    url = base_url + '/artists/'
    if artist_id != -1:
        return requests.get(url + str(artist_id)).json()[param_artist]
    else:
        return ""


def get_all_artists():
    artist_list = []
    artists = fetch_artists()
    for artist in artists:
        artist_list.append(artist[param_name])
    return artist_list


def linear_view_artist(name):
    artist_id = 0
    artists = fetch_artists()
    for artist in artists:
        if artist[param_name].lower() == name.lower():
            artist_id = artist[param_id]
    if artist_id == 0:
        return 0
    return fetch_artist(artist_id)
