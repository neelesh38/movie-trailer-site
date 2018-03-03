# import webbrowser library
import webbrowser


class Movie():
    # class Movie() is used to define instances.
    def __init__(self, movie_title, movie_storyline   # calling constructor
                 , poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
    # show_trailer function is declared to open the webbrowser
        webbrowser.open(self.trailer_youtube_url)
