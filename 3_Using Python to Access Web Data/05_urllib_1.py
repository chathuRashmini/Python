import urllib.request, urllib.parse, urllib.error
# to read url above files has to be imported

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# treate the site as a file
count = dict()

for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    # since this comes from UTF-8 it has to be decoded
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
