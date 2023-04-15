class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

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

