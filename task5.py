class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"
class Pen(Stationery):
    def draw(self):
        return f"Отрисовка предметом {self.title}"

class Pencil(Stationery):
    def draw(self):
        return f"Отрисовка предметом {self.title}"

class Handle(Stationery):
    def draw(self):
        return f"Отрисовка предметом {self.title}"

p = Pen("ручка")
print(p.draw())
pc = Pencil("карандаш")
print(pc.draw())
h = Handle("маркер")
print(h.draw())