class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def mass(self):
        mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Mass of asphalt is - {round(mass)} t')


r = Road(5000, 20)
r.mass()
