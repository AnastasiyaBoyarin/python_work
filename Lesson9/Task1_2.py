class TypedProperty:
    def __init__(self, name, type_name, default=None):
        self.name = "_" + name
        self.type = type_name
        self.default = default if default else type_name()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Type should be %s" % self.type)
        setattr(instance, self.name, value)


class Worker:

    name = TypedProperty("name", str)
    surname = TypedProperty("name", str)

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        result = f"{self.name} {self.surname}"
        return result

    def __str__(self):
        result = f"{self.name} {self.surname}"
        return result

    def get_total_income(self):
        result = f"{sum(self._income.values())}"
        return result


user = Position("Nastya", "Boyarin", "BOSS", 50000, 1250)
print(user.get_full_name())
print(user.position)
print(user.get_total_income())
print(user)

# user = Position(123, 123, "BOSS", 50000, 1250)
# print(user.get_full_name())
# print(user.position)
# print(user.get_total_income())
# print(user)
