movies = {
    "Master" : "11:00 am",
    "Radhe":"3:00 pm",
    "Karnan":"6:00 pm",
    "Bigil" : "9:00 pm"
}

print('Movies that are running in theater are')
for key in movies:
    print(key)

customerRequest = movies.get(input('Enter the movie name you want to know the timing for : '))

if customerRequest ==None:
    print("Requested movie not there ")
else:
    print("Movies timings are ", customerRequest)    