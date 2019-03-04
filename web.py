import json
import requests


#Fetches the JSON object for "artists" or "artist" depending on artist_id flag.
# if artist_id flag is false, get the "artists" JSON object, otherwise get the
# "artist" object.
def fetch_artists(artist_id = False):
    url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'
    if artist_id != False:
        return requests.get(url + artist_id).json()["artist"]
    else:
        return requests.get(url).json()["artists"]

#Creates a list of artist names.
def get_all_artists():
    list = []
    for artist in fetch_artists():
        list.append(artist["name"])
    return list

#Looks for an ID in the "artists" JSON object, based on the name of the artist.
# if the ID is found, request additional artist information from the API,
# otherwise return error values if artist name wasn't found.
def linear_view_artist(name):
    artist_id = 0
    for artist in fetch_artists(): 
       if artist["name"].lower() == name.lower():
            artist_id = artist["id"]
    if artist_id == 0:
        return 0
    return fetch_artists(artist_id)



