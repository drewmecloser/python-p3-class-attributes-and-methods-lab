class Song:
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        
        self.name = name
        self.artist = artist
        self.genre = genre

        
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        self.add_to_artist_count(artist)
        self.add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls):
        """Increments the total song count."""
        cls.count += 1

    @classmethod
    def add_to_artists(cls, artist):
        """Adds a new artist to the artists list if not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls, genre):
        """Adds a new genre to the genres list if not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artist_count(cls, artist):
        """Updates the artist_count dictionary (histogram) for a given artist."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates the genre_count dictionary (histogram) for a given genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1