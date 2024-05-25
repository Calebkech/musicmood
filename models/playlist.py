#!/usr/bin/python3
"""Defines the Playlist class."""

from models.base_model import BaseModel

class Playlist(BaseModel):
    """Represents a playlist entity."""

    def __init__(self, name="", description="", url="", image_url="", owner="", total_tracks=0, *args, **kwargs):
        """Initialize the Playlist.

        Args:
            name (str): The name of the playlist.
            description (str): The description of the playlist.
            url (str): The Spotify URL of the playlist.
            image_url (str): The URL of the playlist's image.
            owner (str): The owner of the playlist.
            total_tracks (int): The total number of tracks in the playlist.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.url = url
        self.image_url = image_url
        self.owner = owner
        self.total_tracks = total_tracks

    def __str__(self):
        """Return a string representation of the Playlist instance."""
        return f"[Playlist] (ID: {self.id}, Name: {self.name})"

    def to_dict(self):
        """Return a dictionary representation of Playlist."""
        playlist_dict = super().to_dict()
        playlist_dict.update({
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "image_url": self.image_url,
            "owner": self.owner,
            "total_tracks": self.total_tracks
        })
        return playlist_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a Playlist instance from a dictionary."""
        return cls(**obj_dict)
