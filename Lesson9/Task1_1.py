class NonNegative:
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Number should be positive")

        instance.__dict__[self.my_attr] = value


class Road:
    weight = 25
    height = 5

    length = NonNegative('length')
    width = NonNegative('width')

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self):
        mass = self.length * self.width * self.weight * self.height / 1000
        print(f'Mass of asphalt is - {round(mass)} t')


r = Road(5000, 20)
r.mass()

r.width = 10
r.length = -20
r.mass()
