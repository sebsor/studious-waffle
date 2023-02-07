current_movies = {
    'Spider-man' : 'Onsdag | 21:30 | Salong 1 ',
    'Bladerunner' : 'Fredag | 22:00 | Salong 1',
    'My little pony' : 'Tisdag | 18:00 | Salong 3',
    'Star Wars' : 'Lördag | 19:00 | Salong 2'
}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None :
    print("Requested showtime isn't playing")
else : 
    print(movie, 'is playing at', showtime)