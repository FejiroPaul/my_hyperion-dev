"""
Program to give recommend another movie after user watches a movie
"""
# importing libraries
import spacy

nlp = spacy.load('en_core_web_md')


def suggest_movie(previous_watch: str) -> str:
    """
    function to generate a movie suggestion from list of movies
    :param previous_watch (string): description of previous movie watched
    :return string : title of a suggested movie with highest similarity to recently watched movie
    """
    watched_movie = nlp(previous_watch)
    movies = {}
    with open("movies.txt", "r") as file:
        line = file.readline()
        while line:
            movie, description = line.strip("\n").split(":")
            description = nlp(description)
            score = watched_movie.similarity(description)
            movies[movie] = score
            line = file.readline()
    return max(movies, key=movies.get)


# get description of recently watched movie
watched_movie = """Will he save their world or destroy it? when 
the Hulk becomes too dangerous for the  Earth, 
the Illuminati trick Hulk into a shuttle and launch
him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk land on the planet Sakaar where he is 
sold into slavery and trained as a gladiator"""

suggested_movie = suggest_movie(watched_movie)
print("a movie you could like is ", suggested_movie)
