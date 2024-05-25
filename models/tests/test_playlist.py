#!/usr/bin/python3
"""Unittest for the Playlist class."""

import unittest
from models.playlist import Playlist

class TestPlaylist(unittest.TestCase):
    """Tests the Playlist class."""

    def setUp(self):
        """Set up a Playlist instance for testing."""
        self.playlist = Playlist(
            name="Test Playlist",
            description="This is a test playlist",
            url="https://open.spotify.com/playlist/test",
            image_url="https://example.com/test.jpg",
            owner="Test User",
            total_tracks=10
        )

    def test_attributes(self):
        """Test if the Playlist instance has the correct attributes."""
        self.assertEqual(self.playlist.name, "Test Playlist")
        self.assertEqual(self.playlist.description, "This is a test playlist")
        self.assertEqual(self.playlist.url, "https://open.spotify.com/playlist/test")
        self.assertEqual(self.playlist.image_url, "https://example.com/test.jpg")
        self.assertEqual(self.playlist.owner, "Test User")
        self.assertEqual(self.playlist.total_tracks, 10)

    def test_to_dict(self):
        """Test if to_dict method returns the correct dictionary representation."""
        playlist_dict = self.playlist.to_dict()
        self.assertEqual(playlist_dict["name"], "Test Playlist")
        self.assertEqual(playlist_dict["description"], "This is a test playlist")
        self.assertEqual(playlist_dict["url"], "https://open.spotify.com/playlist/test")
        self.assertEqual(playlist_dict["image_url"], "https://example.com/test.jpg")
        self.assertEqual(playlist_dict["owner"], "Test User")
        self.assertEqual(playlist_dict["total_tracks"], 10)

    def test_from_dict(self):
        """Test if from_dict method correctly creates a Playlist instance."""
        playlist_dict = {
            "name": "Another Playlist",
            "description": "This is another test playlist",
            "url": "https://open.spotify.com/playlist/another",
            "image_url": "https://example.com/another.jpg",
            "owner": "Another User",
            "total_tracks": 20
        }
        new_playlist = Playlist.from_dict(playlist_dict)
        self.assertEqual(new_playlist.name, "Another Playlist")
        self.assertEqual(new_playlist.description, "This is another test playlist")
        self.assertEqual(new_playlist.url, "https://open.spotify.com/playlist/another")
        self.assertEqual(new_playlist.image_url, "https://example.com/another.jpg")
        self.assertEqual(new_playlist.owner, "Another User")
        self.assertEqual(new_playlist.total_tracks, 20)

    def test_str(self):
        """Test the string representation of the Playlist instance."""
        playlist_str = str(self.playlist)
        expected_str = "[Playlist] (ID: {}, Name: Test Playlist)".format(self.playlist.id)
        self.assertEqual(playlist_str, expected_str)

if __name__ == "__main__":
    unittest.main()
