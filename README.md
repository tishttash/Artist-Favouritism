# Artist-Favouritism

## This you?
You like too many songs on Spotify and add them into too many playlists... but one day you only feel like listening to [insert artist's name here] but oh no you don't remember which of your playlists you've added their tracks to. Well yup this pretty much solves your issue homie.

## What this simple app uses:
- Spotipy wrapper
- OAuth2
- my time and effort

<h2>What does it do, basically?</h2>
Goes through all your user-owned playlists and picks out the tracks by the specified artist. Compiles them into a new playlist for you! 


### Additional Notes: 
- my app's client credentials are ... obviously not in here. make sure you grab them from your own Spotify Developer Dashboard after creating a new app and add them into your own client credentials file to be imported! (mine was named clientcreds, edit the name accordingly)
- remove access from this app via your Spotify account WILL break it, because I didn't bother with the code to handle that. you would have to create a whole new app and redo the authorization process.
- some parts of my code might not seem vErY PyThoNic because I'm pretty nooby so go easy on me <3
- I made this because this was a huge problem I faced believe it or not. Haha. Enjoy the app I didn't bother to make a GUI for it because it seemed too niche.
