#!/usr/bin/python3
"""Unittest for the Song class."""

import unittest
from models.song import Song

class TestSong(unittest.TestCase):
    """Tests the Song class."""

    def setUp(self):
        """Set up a Song instance for testing."""
        self.song = Song(
            name="Test Song",
            artist="Test Artist",
            album="Test Album",
            release_date="2020-01-01",
            duration_ms=200000,
            popularity=50,
            preview_url="https://example.com/preview.mp3",
            genre="Pop",
            energy=0.8,
            valence=0.6,
            danceability=0.7,
            tempo=120.0
        )

    def test_attributes(self):
        """Test if the Song instance has the correct attributes."""
        self.assertEqual(self.song.name, "Test Song")
        self.assertEqual(self.song.artist, "Test Artist")
        self.assertEqual(self.song.album, "Test Album")
        self.assertEqual(self.song.release_date, "2020-01-01")
        self.assertEqual(self.song.duration_ms, 200000)
        self.assertEqual(self.song.popularity, 50)
        self.assertEqual(self.song.preview_url, "https://example.com/preview.mp3")
        self.assertEqual(self.song.genre, "Pop")
        self.assertEqual(self.song.energy, 0.8)
        self.assertEqual(self.song.valence, 0.6)
        self.assertEqual(self.song.danceability, 0.7)
        self.assertEqual(self.song.tempo, 120.0)

    def test_to_dict(self):
        """Test if to_dict method returns the correct dictionary representation."""
        song_dict = self.song.to_dict()
        self.assertEqual(song_dict["name"], "Test Song")
        self.assertEqual(song_dict["artist"], "Test Artist")
        self.assertEqual(song_dict["album"], "Test Album")
        self.assertEqual(song_dict["release_date"], "2020-01-01")
        self.assertEqual(song_dict["duration_ms"], 200000)
        self.assertEqual(song_dict["popularity"], 50)
        self.assertEqual(song_dict["preview_url"], "https://example.com/preview.mp3")
        self.assertEqual(song_dict["genre"], "Pop")
        self.assertEqual(song_dict["energy"], 0.8)
        self.assertEqual(song_dict["valence"], 0.6)
        self.assertEqual(song_dict["danceability"], 0.7)
        self.assertEqual(song_dict["tempo"], 120.0)

    def test_from_dict(self):
        """Test if from_dict method correctly creates a Song instance."""
        song_dict = {
            "name": "Another Song",
            "artist": "Another Artist",
            "album": "Another Album",
            "release_date": "2021-01-01",
            "duration_ms": 210000,
            "popularity": 55,
            "preview_url": "https://example.com/another_preview.mp3",
            "genre": "Rock",
            "energy": 0.85,
            "valence": 0.65,
            "danceability": 0.75,
            "tempo": 125.0
        }
        new_song = Song.from_dict(song_dict)
        self.assertEqual(new_song.name, "Another Song")
        self.assertEqual(new_song.artist, "Another Artist")
        self.assertEqual(new_song.album, "Another Album")
        self.assertEqual(new_song.release_date, "2021-01-01")
        self.assertEqual(new_song.duration_ms, 210000)
        self.assertEqual(new_song.popularity, 55)
        self.assertEqual(new_song.preview_url, "https://example.com/another_preview.mp3")
        self.assertEqual(new_song.genre, "Rock")
        self.assertEqual(new_song.energy, 0.85)
        self.assertEqual(new_song.valence, 0.65)
        self.assertEqual(new_song.danceability, 0.75)
        self.assertEqual(new_song.tempo, 125.0)

if __name__ == "__main__":
    unittest.main()
