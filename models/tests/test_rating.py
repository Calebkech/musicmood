#!/usr/bin/python3
"""Unittest for the Rating class."""

import unittest
from models.rating import Rating

class TestRating(unittest.TestCase):
    """Tests the Rating class."""

    def setUp(self):
        """Set up a Rating instance for testing."""
        self.rating = Rating(
            user_id="user123",
            song_id="song123",
            rating=5
        )

    def test_attributes(self):
        """Test if the Rating instance has the correct attributes."""
        self.assertEqual(self.rating.user_id, "user123")
        self.assertEqual(self.rating.song_id, "song123")
        self.assertEqual(self.rating.rating, 5)

    def test_to_dict(self):
        """Test if to_dict method returns the correct dictionary representation."""
        rating_dict = self.rating.to_dict()
        self.assertEqual(rating_dict["user_id"], "user123")
        self.assertEqual(rating_dict["song_id"], "song123")
        self.assertEqual(rating_dict["rating"], 5)

    def test_from_dict(self):
        """Test if from_dict method correctly creates a Rating instance."""
        rating_dict = {
            "user_id": "user456",
            "song_id": "song456",
            "rating": 3
        }
        new_rating = Rating.from_dict(rating_dict)
        self.assertEqual(new_rating.user_id, "user456")
        self.assertEqual(new_rating.song_id, "song456")
        self.assertEqual(new_rating.rating, 3)

if __name__ == "__main__":
    unittest.main()
