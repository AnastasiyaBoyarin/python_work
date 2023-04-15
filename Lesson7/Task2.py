class Road:
    weight = 25
    height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Mass of asphalt is - {round(mass)} t')


r = Road(5000, 20)
r.mass()
