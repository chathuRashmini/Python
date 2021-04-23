# PYTHON LISTS PART 03

movie = "Harry Potter and the Philosopher's Stone"
print('Movie: ', movie)
print('Length: ', len(movie)) # length of the string

movieS = movie.split() # split the string at each space and output a list of elements(words)
print('After splitting: ', movieS)
print('Length after splitting: ', len(movieS)) # different from the length of the string

roles = 'harry;ron;hermione'
delChar = roles.split(';')
# split at the given delimitter character (in here semicolon ;)
print('Movies with delimitter: ', delChar)
print('Length with delimitter: ', len(delChar))
