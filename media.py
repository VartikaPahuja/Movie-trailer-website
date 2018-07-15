import webbrowser


class Movie():
    """This class provides a way to store movie related information and
       then showing the trailer of the movie.

    Args:
        movie_title (str): The title of the movie.
        movie_storyline (str): The storyline of movie.
        image : Argument for the link of image.
        trailer_youtube : Argument for the link of trailer.

    Attributes:
        title (str): The title of the movie.
        storyline (str): The storyline of movie.
        poster_image_url : Argument for the link of image.
        trailer_youtube_url : Argument for the link of trailer.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        # if we remove word self here then we won't be able to access storyline
        # in other class we can only accesss it in this function only.

        self.poster_image_url = image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



        
   
