#
# movie = 'Gamer'
# rating = 100
#
# result = f'Movie: "{movie}" Rating {rating}'
# print(result)
#
# print()
#
# movie = 'Alien'
# rating = 150
#
# result = f'Movie: "{movie}" Rating {rating}'
# print(result)


# def greet(movie, rating):
#     result = f'Movie: "{movie}" Rating {rating}'
#     print(result)
#
# movie = 'Gamer'
# rating = 100
#
# greet(movie, rating)
#
# greet(rating = 150, movie = 'Alien')

def greet(movie, rating, catalog = 'Kinopoisk'):
    res = f'Site: {catalog} Movie: "{movie}" Rating {rating}'
    return res

name_mov = 'Gamer'

g = greet(name_mov, rating = 275)
# movie = name_mov ='Gamer'
print(g)

g = greet(rating = 100, movie = 'Alien')

print(g)
