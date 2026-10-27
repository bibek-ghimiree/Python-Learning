class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self):
        return f"Book({self.title!r}, {self.pages})"


book = Book("Python Basics", 250)

print(book)
print(repr(book))


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.songs == other.songs


p1 = Playlist(["Song A", "Song B"])
p2 = Playlist(["Song A", "Song B"])

print(len(p1))   # 2
print(p1 == p2)  # True





class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Number(self.value + other.value)

    def __repr__(self):
        return f"Number({self.value})"


a = Number(10)
b = Number(20)

print(a + b)  # Number(30)