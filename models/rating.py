#!/usr/bin/python3
"""Defines the Rating class."""

from models.base_model import BaseModel

class Rating(BaseModel):
    """Represents a rating given by a user."""

    def __init__(self, user_id="", song_id="", rating=0, *args, **kwargs):
        """Initialize the Rating.

        Args:
            user_id (str): The ID of the user giving the rating.
            song_id (str): The ID of the song the rating is for.
            rating (int): The rating value (e.g., 1-5).
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.song_id = song_id
        self.rating = rating

    def to_dict(self):
        """Return a dictionary representation of Rating."""
        rating_dict = super().to_dict()
        rating_dict.update({
            "user_id": self.user_id,
            "song_id": self.song_id,
            "rating": self.rating
        })
        return rating_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a Rating instance from a dictionary."""
        return cls(**obj_dict)
