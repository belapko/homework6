class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f" Машина {self.name} поехала\n"

    def stop(self):
        return f"Машина {self.name} остановилась\n"

    def turn(self, direction):
        return f"Машина {self.name} совершила поворот {direction}\n"

    def show_speed(self):
        return f"Скоросить машины {self.name} равна {self.speed}\n"

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Скоросить превышена!\n"
        else:
            return f"Скорость машина {self.name} = {self.speed}\n"

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Скоросить превышена!\n"
        else:
            return f"Скорость машина {self.name} = {self.speed}\n"

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

t = TownCar(200, "чёрный", "Лада", True)
print(t.go(), t.show_speed(), t.turn("налево"), t.stop())