current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '1:00pm',
                  'Frosty the snowman': '3:00pm',
                  'Christmas Vacation': '5:00pm',
                  }
print("We are showing the following movies:")

for key in current_movies:
    print(key)
movie = input("\n\nwhat movie would you like the showtime for?\n")

print("your move is showing at",current_movies.get(movie))
