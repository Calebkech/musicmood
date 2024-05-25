#!/usr/bin/python3
"""Defines the Feedback class."""

from models.base_model import BaseModel

class Feedback(BaseModel):
    """Represents feedback given by a user."""

    def __init__(self, user_id="", song_id="", comment="", *args, **kwargs):
        """Initialize the Feedback.

        Args:
            user_id (str): The ID of the user giving the feedback.
            song_id (str): The ID of the song the feedback is for.
            comment (str): The comment text of the feedback.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.song_id = song_id
        self.comment = comment

    def to_dict(self):
        """Return a dictionary representation of Feedback."""
        feedback_dict = super().to_dict()
        feedback_dict.update({
            "user_id": self.user_id,
            "song_id": self.song_id,
            "comment": self.comment
        })
        return feedback_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a Feedback instance from a dictionary."""
        return cls(**obj_dict)
