class Movie:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
        self.avaliable = True

    def mark_as_rented(self):
        self.avaliable = False

    def mark_as_avaiable(self):
        self.avaliable = True

    def __str__(self):
        return f"{self.title} ({self.genre})-({self.year})-{"Avaliable" if self.avaliable else "Rented"}"