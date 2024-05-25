#!/usr/bin/python3
"""Defines the Song class."""

from models.base_model import BaseModel

class Song(BaseModel):
    """Represents a song entity."""

    def __init__(self, name="", artist="", album="", release_date="", duration_ms=0, popularity=0, preview_url="", genre="", energy=0.0, valence=0.0, danceability=0.0, tempo=0.0, *args, **kwargs):
        """Initialize the Song.

        Args:
            name (str): The name of the song.
            artist (str): The artist of the song.
            album (str): The album where the song is included.
            release_date (str): The release date of the song.
            duration_ms (int): The duration of the song in milliseconds.
            popularity (int): The popularity of the song.
            preview_url (str): The preview URL of the song.
            genre (str): The genre of the song.
            energy (float): The energy level of the song.
            valence (float): The valence level of the song.
            danceability (float): The danceability level of the song.
            tempo (float): The tempo of the song.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = name
        self.artist = artist
        self.album = album
        self.release_date = release_date
        self.duration_ms = duration_ms
        self.popularity = popularity
        self.preview_url = preview_url
        self.genre = genre
        self.energy = energy
        self.valence = valence
        self.danceability = danceability
        self.tempo = tempo

    def to_dict(self):
        """Return a dictionary representation of Song."""
        song_dict = super().to_dict()
        song_dict.update({
            "name": self.name,
            "artist": self.artist,
            "album": self.album,
            "release_date": self.release_date,
            "duration_ms": self.duration_ms,
            "popularity": self.popularity,
            "preview_url": self.preview_url,
            "genre": self.genre,
            "energy": self.energy,
            "valence": self.valence,
            "danceability": self.danceability,
            "tempo": self.tempo
        })
        return song_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a Song instance from a dictionary."""
        return cls(**obj_dict)
