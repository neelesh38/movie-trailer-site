# import the fresh_tomatoes to link the page with html
import fresh_tomatoes
import media
# Passing arguments to media to open trailer
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# adding title,rating,poster,trailer of movie toy_story in variable toy_story

avatar = media.Movie("Avtar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# adding title,rating,poster,trailer of movie avatar in variable avatar

spyder = media.Movie("Spyder",
                     "Spyder is an upcoming 2017 bilingual Indian spy",
                     "https://upload.wikimedia.org/wikipedia/en/d/de/"
                     "Spyder_film_poster.jpg",
                     "https://www.youtube.com/watch?v=og1zP3u0b4k")

# adding title,rating,poster,trailer of movie spyder

The_Wolf = media.Movie("The Wolf of Wall Street",
                       "It recounts Belfort's perspective on his career",
                       "https://upload.wikimedia.org/wikipedia/en/1/1f/"
                       "WallStreet2013poster.jpg",
                       "https://www.youtube.com/watch?v=iszwuX1AK6A")

# adding title,rating,poster,trailer of movie The_Wolf_of_Wall_Street
The_Hunger_Games = media.Movie("The Hunger Games ",
                               "A real reality show",
                               "https://upload.wikimedia.org/wikipedia/en"
                               "/4/42/HungerGamesPoster.jpg",
                               "https://www.youtube.com/watch?v=4S9a5V9ODuY")
# adding title,rating,poster,trailer of movie The_Hunger_Games
It = media.Movie("It",
                 "American Horrer Movie",
                 "https://upload.wikimedia.org/wikipedia/en"
                 "/5/5a/It_%282017%29_poster.jpg",
                 "https://www.youtube.com/watch?v=FnCdOQsX5kc")
# adding title,rating,poster,trailer of movie It in variable It

movies = [toy_story, avatar, spyder,
          The_Wolf, The_Hunger_Games, It]
# Making the array to call the function from media
fresh_tomatoes.open_movies_page(movies)
