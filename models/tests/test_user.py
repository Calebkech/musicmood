import unittest
from models.playlist import Playlist
from models.base_model import BaseModel

class TestPlaylist(unittest.TestCase):
    """Test cases for the Playlist model."""

    def setUp(self):
        """Set up test environment."""
        self.playlist = Playlist(
            name="Test Playlist",
            description="This is a test playlist",
            url="https://open.spotify.com/playlist/test",
            image_url="https://example.com/test.jpg",
            owner="Test User",
            total_tracks=10
        )

    def tearDown(self):
        """Tear down test environment."""
        del self.playlist

    def test_attributes(self):
        """Test that Playlist attributes are correctly initialized."""
        self.assertEqual(self.playlist.name, "Test Playlist")
        self.assertEqual(self.playlist.description, "This is a test playlist")
        self.assertEqual(self.playlist.url, "https://open.spotify.com/playlist/test")
        self.assertEqual(self.playlist.image_url, "https://example.com/test.jpg")
        self.assertEqual(self.playlist.owner, "Test User")
        self.assertEqual(self.playlist.total_tracks, 10)

    def test_is_instance_of_base_model(self):
        """Test that Playlist is an instance of BaseModel."""
        self.assertTrue(isinstance(self.playlist, BaseModel))

    def test_to_dict(self):
        """Test the to_dict method creates a dictionary with the correct attributes."""
        playlist_dict = self.playlist.to_dict()
        self.assertEqual(playlist_dict["name"], "Test Playlist")
        self.assertEqual(playlist_dict["description"], "This is a test playlist")
        self.assertEqual(playlist_dict["url"], "https://open.spotify.com/playlist/test")
        self.assertEqual(playlist_dict["image_url"], "https://example.com/test.jpg")
        self.assertEqual(playlist_dict["owner"], "Test User")
        self.assertEqual(playlist_dict["total_tracks"], 10)
        self.assertEqual(playlist_dict["__class__"], "Playlist")
        self.assertTrue("created_at" in playlist_dict)
        self.assertTrue("updated_at" in playlist_dict)

    def test_str(self):
        """Test the string representation of the Playlist instance."""
        playlist_str = str(self.playlist)
        expected_str = "[Playlist] (ID: {}, Name: Test Playlist)".format(self.playlist.id)
        self.assertEqual(playlist_str, expected_str)

if __name__ == "__main__":
    unittest.main()
