from spotify_api import SpotifyAuth
from requests import get

class SpotifyClient(SpotifyAuth):
    def __init__(self):
        super().__init__()
        self.api_url = "https://api.spotify.com/v1"
    
    def search_playlists(self, query, limit=10):
        headers = self.get_auth_header()
        search_url = f"{self.api_url}/search"
        params = {
            "q": query,
            "type": "playlist",
            "limit": limit
        }
        response = get(search_url, headers=headers, params=params)
        return response.json()
