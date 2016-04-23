#In this Python File we define the class Movie and its constructor
# Each instance of the class movie will house movie data and will 
# contain the method show_trailer
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title,movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
