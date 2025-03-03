# CODE UPDATED: 3 MARCH 2025

import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from clientcreds import user_id, client_id, client_secret

SPOTIPY_USER_ID = user_id
SPOTIPY_CLIENT_ID = client_id
SPOTIPY_CLIENT_SECRET = client_secret
SPOTIPY_REDIRECT_URL = "http://127.0.0.1:9090"
SCOPES = "playlist-read-private,playlist-modify-private"
user_owned_playlists_id = []   # list of user-owned playlist ids
playlist_items_add = []  # list of track IDs to add into playlist


# performing oauth for user
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URL,
    scope=SCOPES
))

# player inputs for artist name
artist_name = input("Enter the artist's name: ")
# playlists_offest = input("\nStarting playlist position (integer) to search: ")
print(f"\nSearching through your playlists...")

# creating playlist for user
sp.user_playlist_create(
    SPOTIPY_USER_ID,
    f"{artist_name} Favouritism",
    public=False,
    collaborative=False,
    description=f"sometimes you just gotta listen to {artist_name} and {artist_name} only"
)
# get id of this newly created playlist
new_playlist = sp.current_user_playlists(limit=1)
new_playlist_id = new_playlist['items'][0]['id']

# get current user's OWNED playlists
user_playlists1 = sp.current_user_playlists(limit=50)
user_playlists2 = sp.current_user_playlists(offset=50)

# print(json.dumps(user_playlists, indent=4))
for playlist in user_playlists1['items']:
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    playlist_owner = playlist['owner']['id']
    # print(f"Playlist name: {playlist_name}")
    
    if playlist_owner == SPOTIPY_USER_ID:
        user_owned_playlists_id.append(playlist_id)

for playlist in user_playlists2['items']:
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    playlist_owner = playlist['owner']['id']
    # print(f"Playlist name: {playlist_name}")
    
    if playlist_owner == SPOTIPY_USER_ID:
        user_owned_playlists_id.append(playlist_id)

# print fetched playlist details for user to see
print(f"\nPlaylists owned by {SPOTIPY_USER_ID}: {user_owned_playlists_id}")
print(f"\nFetching tracks by {artist_name}.....")


# get the tracks by particular artist in the user's OWNED playlists
for id in user_owned_playlists_id:
    user_playlists_items = sp.playlist_tracks(id)
    # print(json.dumps(user_playlists_items, indent=4))
    for items in user_playlists_items['items']:
        for artist in items['track']['artists']:
            if artist['name'] == artist_name:
                if items['track']['uri'] not in playlist_items_add:
                    playlist_items_add.append(items['track']['uri'])
                    print(".")
    # to extend the limit of 100 tracks to read in a playlist
    while user_playlists_items['next']:
        user_playlists_items = sp.next(user_playlists_items)
        for items in user_playlists_items['items']:
            for artist in items['track']['artists']:
                if artist['name'] == artist_name:
                    if items['track']['uri'] not in playlist_items_add:
                        playlist_items_add.append(items['track']['uri'])
                        print(".")

print(f"\nTracks to add in new playlist: {len(playlist_items_add)}")

# add the list of playlist_items_add
sp.playlist_add_items(new_playlist_id, playlist_items_add)
print(f"\nAll tracks in your playlists by {artist_name} have been added to a newly created playlist.\n")