# Artist-Favouritism
For when I have the urge to listen to only the songs I like from a specific artist.

## What it does
Goes through all my created playlists and picks out the tracks by the specified artist.  
Compiles them into a new playlist (which I will proceed to delete after i get sick of loooping it...)


## How to run:
1. Can only be run locally for now 
2. Go to spotify developer and create an app
3. Find your client id and client secret credentials and add it to the 'clientcreds.py' file
4. Find your user id and add it to the 'clientcreds.py' file
5. Run the script locally with python3


## Troubleshooting:
If refresh token has been revoked:
1. Remove app from your spotify account
2. Delete .cache file (hidden file on mac, use shift+cmd+. to unhide)
3. Re-run artist_favouritism.py


## Authors' Notes:
- my code is quite trash honestly. but as long as it works then it works ;)
- I made this mainly for my own problem haha. But have since sent this script to a few friends who saw it and saw the use-cases for it too. happy to share!
- might make a UI for it some day when i'm free
