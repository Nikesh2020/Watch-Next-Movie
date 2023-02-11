"""
T38 Compulsory Task 2:
------------------
File name: watch_next.py
Author: Nikesh Chavda
Student ID: NC22110005394
Notes:
Assumptions:
Dependencies: please install spaCy:
Type the following commands in command line: -

pip3 install spacy
python3 -m spacy download en_core_web_md
----------------OR----------------------
pip install spacy
python -m spacy download en_core_web_md
"""

import spacy
nlp = spacy.load('en_core_web_md')          # use the more advanced language model

# store the movie to compare(the hulk)  into a string in the format "movie-name :movie-description"
hulk_movie = "Planet Hulk :Will he save their world or destroy it? When the Hulk becomes too dangerous for the " \
          "Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk" \
          " can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and " \
          "trained as a gladiator.” The function takes in the description as a parameter and return the title of " \
          "the most similar movie."


# a function to return which movies a user would watch next based on the movie they input as a parameter to the function
def watch_next(my_movie):

    my_movie_title, movie_description_to_compare = my_movie.split(' :')         # extract the movie description from the
                                                                                # movie to compare

    movies_desc_dict = {}                                                       # dictionary buffer to store movies from
                                                                                # text file
    file = None
    try:
        file = open('movies.txt', 'r')                                          # open the movies.txt
        movies_list = file.readlines()                                          # read in all movies from text file

        for movie in movies_list:                                               # for each movie in the list
            movie_title, movie_description = movie.strip('\n').split(' :')      # remove the newline and split its title
            movies_desc_dict[movie_title] = movie_description                   # and description and save the
                                                                                # information into a dictionary

    except FileNotFoundError as error:                                          # Handle any file errors
        print("The movies.txt file that you are trying to open does not exist")
        print(error)
    finally:                                                                    # and close the file
        if file is not None:
            file.close()

    nlp_movie_description_to_compare = nlp(movie_description_to_compare)   # apply model to movie-description-to-compare

    # for each movie description in the dictionary apply nlp model to it then compare it's similarity to the
    # movie-description-to-compare, and store it similarity value to the similarity dictionary
    similarity_dict = {}
    for movie in movies_desc_dict.keys():
        similarity_dict[movie] = nlp(movies_desc_dict[movie]).similarity(nlp_movie_description_to_compare)

    # return the key of the maximum similarity value from the similarity dictionary item
    return max(similarity_dict, key=similarity_dict.get)

# print out the movie to watch next
print(watch_next(hulk_movie))
