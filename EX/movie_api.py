from movie_model import MovieModel


def callMovieApi(page=1):
    import requests

url = '''
https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=2
'''

    response = requests



def convert_model(movies):
    list = []

    for movie in movies:
       movie_model = MovieModel(movie.title, movie.rating, movie.medium_cover_image)
       list.append(movie_model)

    return list