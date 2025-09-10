class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__ (self):
        return f"{self.album_name}, {self.album_artist}, {self.number_of_songs}"
def bubble_sort(albums):
    n = len(albums)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if albums[j].number_of_songs > albums[j+1].number_of_songs:
                albums[j].number_of_songs, albums[j+1].number_of_songs = albums[j+1].number_of_songs, albums[j].number_of_songs
                swapped = True
        if not swapped:
            break
    return albums
def binary_search(target, items):
    low, high = 0, len(items) - 1
    while high >= low:
        mid = (low + high) // 2
        if items[mid].album_name == target:
            return mid
        elif items[mid].album_name < target:
            low = mid + 1
        else:
            high = mid-1
    return None

album1 = Album("Graduation", 15, "Kanye west")
album2 = Album("To Pimp a Butterfly", 12, "Kendrick Lamar")
album3 = Album("A Moon Shaped Pool", 10, "Radiohead")
album4 = Album("Currents", 9, "Tame Impala")
album5 = Album("Alfredo 2", 12, "Freddie Gibbs")
album6 = Album("Dark Side of the Moon", 9, "Pink Floyd")
album7 = Album("Oops!... I Did it Again", 16, "Britney Spears")

albums1 = [album1, album2, album3, album4, album5]
sort = bubble_sort(albums1)

print([str(item) for item in sort])

sort.append(sort[0])
sort[0] = sort[1]
sort_len = len(sort)
sort[1] = sort[sort_len - 1]
sort.pop()
print([str(item) for item in sort])

albums2 = [album1, album2, album3, album4, album5, album6, album7]
albums2.sort(key=lambda album: album.album_name)
print([str(item) for item in albums2])

print(binary_search("Dark Side of the Moon", albums2))