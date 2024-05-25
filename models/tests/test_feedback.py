#!/usr/bin/python3
"""Unittest for the Feedback class."""

import unittest
from models.feedback import Feedback

class TestFeedback(unittest.TestCase):
    """Tests the Feedback class."""

    def setUp(self):
        """Set up a Feedback instance for testing."""
        self.feedback = Feedback(
            user_id="user123",
            song_id="song123",
            comment="This is a great song!"
        )

    def test_attributes(self):
        """Test if the Feedback instance has the correct attributes."""
        self.assertEqual(self.feedback.user_id, "user123")
        self.assertEqual(self.feedback.song_id, "song123")
        self.assertEqual(self.feedback.comment, "This is a great song!")

    def test_to_dict(self):
        """Test if to_dict method returns the correct dictionary representation."""
        feedback_dict = self.feedback.to_dict()
        self.assertEqual(feedback_dict["user_id"], "user123")
        self.assertEqual(feedback_dict["song_id"], "song123")
        self.assertEqual(feedback_dict["comment"], "This is a great song!")

    def test_from_dict(self):
        """Test if from_dict method correctly creates a Feedback instance."""
        feedback_dict = {
            "user_id": "user456",
            "song_id": "song456",
            "comment": "Not my favorite."
        }
        new_feedback = Feedback.from_dict(feedback_dict)
        self.assertEqual(new_feedback.user_id, "user456")
        self.assertEqual(new_feedback.song_id, "song456")
        self.assertEqual(new_feedback.comment, "Not my favorite.")

if __name__ == "__main__":
    unittest.main()
