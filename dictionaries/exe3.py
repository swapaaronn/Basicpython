name=input("enter a name")
age=int(input("enter a age"))
fav_movie=input("enter a movie").split(',')
fav_song=input("enter a song").split(',')
x={"name":name,'age':age,"fav_movie":fav_movie,"fav_song":fav_song}
value=x.type()
print(x)