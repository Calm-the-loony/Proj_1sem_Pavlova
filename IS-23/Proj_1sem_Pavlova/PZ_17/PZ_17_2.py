# Создайте класс "Фрукт", который содержит информацию о наименовании и весе 
# фрукта. Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса 
# "Фрукт" и содержат информацию о цвете
class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Apple(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

class Orange(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

# Пример использования классов
fruit = Fruit("Фрукт", 100)
print(fruit.name)  # Выводит: Фрукт
print(fruit.weight)  # Выводит: 100

apple = Apple("Яблоко", 200, "Красное")
print(apple.name)  # Выводит: Яблоко
print(apple.weight)  # Выводит: 200
print(apple.color)  # Выводит: Красное
