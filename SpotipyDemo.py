import spotipy # The api used to access spotify information.
from spotipy.oauth2 import SpotifyClientCredentials # Used for authenticating the user for spotify.
import json # Used for parsing the result from spotify.

#### Notes before using ####
# The spotipy API must be installed. This can be done through a variety of ways, ask me to let me know how you're doing it.
# The terminal command for this is (using the pip package installer):
# pip install spotipy
# But you might not want to download it this way, just let me know how you're doing this.
#
# The client_credintials manager uses a client_id and client_secret string.
# If you go to https://developer.spotify.com/dashboard/login
# you can log in with a spotify account (I guess just make an account for this project)
# it will let you register your project and once you do, you can get your client_id and client_secret codes and paste them here.

# Initialize authentication. Don't worry too much about this.
client_credentials_manager = SpotifyClientCredentials(client_id='7ab73ce631054c37a6c59c355b9fadbf', client_secret='46f00549e80a48c1b215f1e21bf89d8f')

# Create a spotipy connection. Also don't worry too much about this.
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# This is the search string. There are a variety of ways to actually set this (i.e. user input, a web interface, etc.),
# let me know if you need help with this
search_str = 'Blackbird Beatles'

# This searches spotify. It'll return a json formatted string with a ton of information about every search result it finds.
# Depending on what you need, we can parse through it and find the information you want to display about each search.
# Here, I just printed the name of the song and the artist.
search_result = sp.search(search_str)

# Loops through every search result.
for result in search_result["tracks"]["items"]:
    # Prints the song name and artist.
    print(result["name"] + " By: " + result["artists"][0]["name"])

    # Contacts spotify asking for the json formatted string with the search results features.
    # Once again, depending on the features you want, this can be edited.
    # Here's an example list of features we can find:
    # https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/
    info = sp.audio_features(result["external_urls"]["spotify"])

    # Prints out the BPM for the song.
    print("BPM: " + info[0]["tempo"])
