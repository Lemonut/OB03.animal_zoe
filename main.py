import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, sound="Чирик-чирик"):
        super().__init__(name, age)
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издаёт звук: {self.sound}")

    def eat(self):
        print(f"{self.name} питается насекомыми и семенами.")

class Mammal(Animal):
    def __init__(self, name, age, sound="Рррр"):
        super().__init__(name, age)
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издаёт звук: {self.sound}")

    def eat(self):
        print(f"{self.name} может быть травоядным или плотоядным.")

class Reptile(Animal):
    def __init__(self, name, age, sound="Шшшш"):
        super().__init__(name, age)
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издаёт звук: {self.sound}")

    def eat(self):
        print(f"{self.name} питается мелкими животными или насекомыми.")

# Полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Класс сотрудников
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        pass

# Подкласс ZooKeeper
class ZooKeeper(Employee):
    def work(self):
        print(f"{self.name} кормит животных.")

# Подкласс Veterinarian
class Veterinarian(Employee):
    def work(self):
        print(f"{self.name} лечит животных.")

# Класс зоопарка (композиция)
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee.name}, должность: {employee.position}")

    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.name}, возраст {animal.age}")

    def show_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee.name}, {employee.position}")

    # Сохранение данных в файл
    def save_to_file(self, filename="zoo_data.json"):
        data = {
            "name": self.name,
            "animals": [{"name": a.name, "age": a.age, "type": a.__class__.__name__} for a in self.animals],
            "employees": [{"name": e.name, "position": e.position} for e in self.employees],
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Данные зоопарка сохранены.")

    # Загрузка данных из файла
    def load_from_file(self, filename="zoo_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            self.name = data["name"]
            self.animals = [Animal(a["name"], a["age"]) for a in data["animals"]]
            self.employees = [Employee(e["name"], e["position"]) for e in data["employees"]]
            print("Данные зоопарка загружены.")
        except FileNotFoundError:
            print("Файл с данными не найден.")

# Создание зоопарка и объектов
zoo = Zoo("Городской Зоопарк")

# Добавление животных
parrot = Bird("Попугай", 2)
elephant = Mammal("Слон", 10)
crocodile = Reptile("Крокодил", 5)

zoo.add_animal(parrot)
zoo.add_animal(elephant)
zoo.add_animal(crocodile)

# Добавление сотрудников
keeper = ZooKeeper("Алексей", "Смотритель")
vet = Veterinarian("Мария", "Ветеринар")

zoo.add_employee(keeper)
zoo.add_employee(vet)

# Демонстрация методов
zoo.show_animals()
zoo.show_employees()

# Проверка полиморфизма
animal_sound([parrot, elephant, crocodile])

# Сохранение данных
zoo.save_to_file()

# Загрузка данных (при следующем запуске программы)
# zoo.load_from_file()