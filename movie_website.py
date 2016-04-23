#This is the file that when run, builds the actual movie website

#media is where the Movie class is defined
import media

#import the html and python functions needed to run program
import fresh_tomatoes

#Instantiate 6 movies
toy_story = media.Movie("Toy Story", 
			"A story of a boy and his toys that come to life",
			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
			"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", 
			"A marine on an alien planet", 
			"http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
			"https://www.youtube.com/watch?v=d1_JBMrrYw8")

shawshank = media.Movie("The Shawshank Redemption", 
			"Some awesomeness followed by subsequent awesomeness", 
			"http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
			"https://www.youtube.com/watch?v=6hB3S9bIaco")

beautiful = media.Movie("A Beautiful Mind", 
			"A genius makes a huge breakthrough in Economics, goes crazy, and then wins a Nobel Prize",
			"http://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg", 
			"https://www.youtube.com/watch?v=aS_d0Ayjw4o")

interstellar = media.Movie("Interstellar", 
			"Apocalypic action(ish)/drama about faraway planets, farms,"
			" blackholes, murder and the very nature of time and space", 
			"http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
			"https://www.youtube.com/watch?v=0vxOhd4qlnA")

sound_of_music = media.Movie( "The Sound of Music", 
			"A nun wins the heart of 6 mother-less children and eventually their father"
			" through song. Then the Nazis show up.", 
			"http://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
			"https://www.youtube.com/watch?v=UY6uw3WpPzY")

crash = media.Movie("Crash", 
			"Some stuff happens to some people in LA", 
			"http://upload.wikimedia.org/wikipedia/en/d/d0/Crash_ver2.jpg", 
			"https://www.youtube.com/watch?v=rVJRcEt4TMM")

#Create an array of the Movie objects, and then 
movies = [shawshank,beautiful,crash,sound_of_music,interstellar,avatar]

#pass this array to the open_movies_page function
fresh_tomatoes.open_movies_page(movies)
