# 1. Using the Python PIP Command create a 'requirements txt'
# file from the Terminal/command-prompt of your system?

pip freeze > requirements.txt

# 2. Using Python PIP Command install the flask module <2.0 into your system?

pip install "Flask<2.0"

# 3. Vist the URL and convert the UML Diagram into Python class Model and method

class AudioFile:
    def __init__(self, name, url, genre):
        self.name = name
        self.url = url
        self.genre = genre
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0

class Playlist:
    def __init__(self, name):
        self.name = name
        self.audios = []

    def add_audio(self, audio_file):
        self.audios.append(audio_file)

    def search_audio(self, name):
        return [audio for audio in self.audios if audio.name == name]

    def average_playlist_rating(self):
        total_ratings = sum(audio.average_rating() for audio in self.audios)
        return total_ratings / len(self.audios) if self.audios else 0

class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def search_playlist(self, name):
        return next((playlist for playlist in self.playlists if playlist.name == name), None)

    def rate_audio(self, playlist_name, audio_name, rating):
        playlist = self.search_playlist(playlist_name)
        if playlist:
            audio = playlist.search_audio(audio_name)
            if audio:
                audio[0].add_rating(rating)


