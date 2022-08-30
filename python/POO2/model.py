from calendar import week


class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    def give_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()
    
    def __str__(self):
        return f'{self._name} - {self.year} ; {self._likes} Likes'

class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self._name} - {self.year} - {self.duration} min ; {self._likes} Likes'
        
class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self._name} - {self.year} - {self.seasons} seasons ; {self._likes} Likes'
        
class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    @property
    def listing(self):
        return self._programs

    def __len__(self):
        return len(self._programs)

avengers = Movie("avengers - infinity war", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Movie("scary movie", 1999, 100)
daredevil = Serie("daredevil", 2016, 2)

avengers.give_like()
tmep.give_like()
tmep.give_like()
tmep.give_like()
tmep.give_like()
daredevil.give_like()
daredevil.give_like()
daredevil.give_like()
daredevil.give_like()
atlanta.give_like()
atlanta.give_like()

movies_and_series = [avengers, atlanta, daredevil, tmep]
weekend_playlist = Playlist('Weekend', movies_and_series)

print(f'Extend of Playlist: {len(weekend_playlist)}')

print(weekend_playlist[0])

for program in weekend_playlist.listing:
    print(program)
