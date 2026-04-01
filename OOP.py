"""*Python OOP պարզ խնդիրներ*"""
import math

"""1. Ստեղծել Person class, որը ունի name եւ age։
Գրել մեթոդ introduce() որը տպում է
Hi, my name is John, and I am 20."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'Hi, my name is {self.name}, and I am {self.age}')

p = Person("John", 20)
p.introduce()

"""2. Ստեղծել Dog class։
Ունի name եւ breed։
Գրել bark() մեթոդ, որը տպում է
Rex says Woof!"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f'{self.name} says, {self.breed}')

d = Dog("Rex", "Woof")
d.bark()

"""3. Ստեղծել Car class։
Ունի brand եւ year։
Գրել մեթոդ info() որը վերադարձնում է մեքենայի տվյալները։"""

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f'Car information, {self.brand}, {self.year}'

car = Car("BMW", 2026)
print(car.info())

"""Ստեղծել Student class։
Ունի name եւ grade։
Գրել մեթոդ is_passed() որը վերադարձնում է True եթե գնահատականը ≥ 50։"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def is_passed(self):
        return True if self.grade >= 50 else False

s=Student("Anna", 51)
print(s.is_passed())

"""5. Ստեղծել Book class։
Ունի title եւ author։
Գրել մեթոդ describe()։"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def describe(self):
        return f'{self.title}, {self.author}'
book = Book("Python for beginners", "unknow author")
print(book.describe())

"""6. Ստեղծել Rectangle class։
Ունի width եւ height։
Գրել մեթոդներ
● area()
● perimeter()"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(10, 20)
print(rectangle.area())
print(rectangle.perimeter())

"""7. Ստեղծել Circle class։
Ունի radius։
Գրել մեթոդ area()։"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
circle = Circle(9)
print(circle.area())

"""8. Ստեղծել BankAccount class։
Ունի
● owner
● balance"""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def info_balance(self):
        print(f'{self.owner} owns {self.balance}SEK')
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f'{self.owner} does not have enough SEK')
    def deposit(self, amount):
        self.balance += amount


bacc = BankAccount("Anna", 100)
bacc.withdraw(100)
bacc.deposit(100)



"""9. Ստեղծել Laptop class։
Ունի
● brand
● ram
Գրել մեթոդ upgrade_ram() որը ավելացնում է RAM-ը։"""
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram
    def upgrade_ram(self, amount):
        self.ram += amount
laptop = Laptop("HP", 8)
laptop.upgrade_ram(8)
print(laptop.ram)

"""10. Ստեղծել Movie class։
Ունի
● title
● rating
Գրել մեթոդ is_good() եթե rating ≥ 7 վերադարձնի True։"""

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
    def is_good(self):
        return True if self.rating >= 7 else False

movie = Movie("Disney", 8)
print(movie.is_good())

"""11. Ստեղծել User class։
Ունի username եւ password։
Գրել մեթոդ check_password(p)։"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, p):
        return self.password == p

a = User("John", 1234)

b = input("Enter your username: ")
c = int(input("Enter your password: "))

if a.username == b and a.check_password(c):
    print("Login successful")
else:
    print("Wrong username or password")

"""12. Ստեղծել Temperature class։
Ունի celsius։
Գրել մեթոդ to_fahrenheit()։"""
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

t = Temperature(27)
print(t.to_fahrenheit())

"""13. Ստեղծել Counter class։
Ունի value։
Գրել մեթոդներ
● increment()
● reset()"""

class Counter:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1
        return self.value

    def reset(self):
        self.value = 0
        return self.value

v = Counter(11)
print(v.increment())
print(v.reset())

"""14. Ստեղծել Song class։
Ունի
● title
● artist
Գրել մեթոդ play()։"""
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    def play(self):
        return f'{self.title}, {self.artist}'
music = Song("Nueva York", "Bad Bunny")
print(music.play())

"""15. Ստեղծել Animal class։
Ունի name։
Գրել մեթոդ speak()։"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name}, {self.age}'

a = Animal("Cow", "muuuh")
print(a.speak())

"""16. Ստեղծել Product class։
Ունի
● name
● price
Գրել մեթոդ discount(percent)։"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def discount(self, percent):
        self.price -= self.price * percent / 100
        return self.price

p = Product("Laptop", 1000)
print(p.discount(20))

"""17. Ստեղծել Light class։
Ունի is_on։
Մեթոդներ
● turn_on()
● turn_off()"""
class Light:
    def __init__(self):
        self.is_on = False # ist ausgeschaltet

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

light = Light()

light.turn_off()
print(light.is_on)

light.turn_off()
print(light.is_on)

"""18. Ստեղծել Timer class։
Ունի seconds։
Մեթոդ countdown() որը նվազեցնում է ժամանակը։"""
class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def countdown(self):
        if self.seconds > 0:
            self.seconds -= 1
        return self.seconds

count_seconds = Timer(4)
print(count_seconds.countdown())
print(count_seconds.countdown())
print(count_seconds.countdown())

"""19. Ստեղծել Password class։
Ունի value։
Մեթոդ is_strong() եթե երկարությունը ≥ 8։"""
class Password:
    def __init__(self, value):
        self.value = value

    def is_strong(self):
        return len(self.value) >= 8


password_value = Password('12345')
print(password_value.is_strong()) # False

password_value2 = Password('Aa123455')
print(password_value2.is_strong()) # True

"""20. Ստեղծել Team class։
Ունի
● name
● players
Մեթոդ add_player(player)։"""
class Team:
    def __init__(self,name):
        self.name = name
        self.players = []
    def add_player(self, player):
        self.players.append(player)

new_player = Team("SSK")
print(new_player.players)

"""21. Ստեղծել ShoppingCart class։
Ունի items list։
Մեթոդներ
● add_item()
● total_items()"""
class ShoppingCart:
    def __init__(self):
        # Wir brauchen hier keine Parameter in __init__,
        # da der Warenkorb leer startet.
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_items(self):
        # Da "items" eine Liste von Strings (Namen) ist,
        # gibt len() die Anzahl der Elemente zurück.
        return len(self.items)


my_cart = ShoppingCart()

my_cart.add_item("Bag")
my_cart.add_item("Shoes")
print(my_cart.total_items())

"""22. Ստեղծել GameCharacter class։
Ունի
● name
● health
Մեթոդ take_damage(amount)։"""
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        #Gesundheit darf nicht negativ sein
        if self.health < 0:
            self.health = 0
        return self.health

c=GameCharacter("John", 100)
print(c.take_damage(100))

"""23. Ստեղծել Playlist class։
Ունի songs list։
Մեթոդ add_song()։"""
class Playlist:
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)

lst = Playlist()
lst.add_song("Song 1")
lst.add_song("Song 2")
print(lst.songs)

"""24. Ստեղծել Clock class։
Ունի
● hour
● minute
Մեթոդ show_time()։"""
class Clock:
    def __init__(self):
        self.hour = hour
        self.minute = minute
    def show_time(self):
        return self.hour, self.minute

hour, minute = 2, 12
clock = Clock()
print(hour, minute)

"""25. Ստեղծել Email class։
Ունի
● sender
● receiver
Մեթոդ send()։"""
class Email:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        # erstelle eine Nachricht, die Absender und Empfänger nutzt
    def send(self):
        msg = f"Email from {self.sender} to {self.receiver} has been sent."
        return msg

my_email = Email("Alis", "Lea")
print(my_email.send())

"""26. Ստեղծել Pet class։
Ունի
● name
● hunger
Մեթոդ feed() որը նվազեցնում է hunger-ը։"""
class Pet:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger
    def feed(self, amount):
        self.hunger -= amount
pet = Pet("Dog", "Cat")
print(pet.feed())


"""27. Ստեղծել Dice class։
Մեթոդ roll() որը վերադարձնում է պատահական թիվ 1–6։"""
import random
class Dice:
    def roll(self):
        # random.randint(1, 6) gibt eine Zahl zwischen 1 und 6 zurück
        return random.randint(1, 6)
my_dice = Dice()
print(my_dice.roll())
print(my_dice.roll())

"""29. Ստեղծել Battery class։"""
class Battery:
    def __init__(self):
        # Die Batterie startet bei 100%
        self.level = 100
    def charge(self,amount):
        if self.level + amount >= 100:
            self.level = 100
        else:
            self.level = self.level + amount

    def use(self, amount):
        if self.level <= 0:
            self.level = 0
        else:
            self.level -= amount

my_phone = Battery()
print(my_phone.use(20))
print(my_phone.use(90))
print(my_phone.charge())

"""30. Ստեղծել BankCard class։
Ունի
● owner
● balance
Մեթոդներ
● pay(amount)
● add_money(amount)"""


class BankCard:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount


    def pay(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
            self.balance -= amount

card = BankCard("Armen", 500)
print(card.deposit(200))  # Balance: 700
print(card.withdraw(1000))  # "Insufficient funds!"
print(card.withdraw(300)) # Balance: 400




"""31. Private salary + raise method
● _salary
● մեթոդ → increase_salary(percent)"""
class Salary:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def increase_salary(self, percent):
        if percent > 0:
            self._salary += self._salary * (percent / 100)
            print(f"Salary increased by {percent}%. New salary: {self._salary}")
        else:
            raise ValueError("Increase percentage must be greater than zero.")

employee = Salary("Alice", 5000)
employee.increase_salary(10)

"""32. Protected speed inheritance
● _speed → subclass օգտագործի"""
class ProtectedSpeed:
    def __init__(self, name, speed):
        self.name = name
        self._speed = speed

class Car(ProtectedSpeed):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    def display_speed(self):
        print(f"The speed of {self.name} is {self._speed} km/h")

my_car = Car("Tesla", 250)
my_car.display_speed()

"""33. Secret key (__key)
● փորձել դրսից հասնել"""
class SecretKey:
    def __init__(self, key):
        self.__key = key
s= SecretKey("")
s.key()


"""34. Password hash simulation
● պահել private
● public method → check(password)"""
class Password:
    def __init__(self, password):
        self.__password = password
    def check(self, password):
        if self.__password == password:
            return True
        else:
            raise ValueError("Incorrect password")

user_password = Password("A1234")
print(user_password.check(""))

"""35. Read-only ID
● id → constructor-ում տրվում է
● չի կարելի փոխել"""
class ID:
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id

    def read_id(self):
        try:
            user.id = 102
        except AttributeError as e:
            print(f"Error: {e}")

user = ID(101)
print(user.id)

"""36. Bank անվտանգություն
● balance private
● փոփոխվում է միայն մեթոդներով"""
class Bank:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
            return True

account = Bank(100)
account.deposit(50)
account.withdraw(30)

"""37. File handler
● _path private
● մեթոդ → read()"""


def __init__(self, path):
    self.__path = path

def read(self):
    try:
        with open(self.__path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"

"""38. Game score guard
● score չի կարող նվազել"""
class GameScore:
    def __init__(self, initial_score=0):
        self._score = initial_score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < self._score:
            print(f"Score cannot decrease from {self._score} to {value}!")
        else:
            self._score = value


player = GameScore(100)
player.score = 150
print(f"Current Score: {player.score}")
player.score = 80
print(f"Current Score: {player.score}")

"""39. Employee bonus hidden
● private bonus
● method → calculate total salary"""
class Employee:
    def __init__(self, name, salary, bonus=0):
        self.name = name
        self.salary = salary
        self.__bonus = bonus

    def get_total_salary(self):
        total = self.salary + self.__bonus
        return total

emp = Employee("John", 1500, 500)

print(f"Employee: {emp.name}")
print(f"Base Salary: ${emp.salary}")
print(f"Total Pay +ink bonus: ${emp.get_total_salary()}")

"""40. API key protected
● _api_key
● public method → simulate request"""
class APIKey:
    def __init__(self, api_key):
        self.__api_key = api_key
    @property
    def api_key(self):
        return self.__api_key
    def simulate_request(self, endpoint):
        if not self.__api_key:
            return " No API key provided."
        print(f"Connecting to {endpoint}...")
        print(f"Using credentials: {self.__api_key[:4]}") #Mask
        return "Request Successful: 200 OK"


service = APIKey("7892341125")
response = service.simulate_request("userdata")
print(response)

"""41–50. Inheritance + super()

41. Animal → Dog override
● sound() override"""
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

my_dog = Dog()
my_dog.sound()
my_cat = Cat()
my_cat.sound()
animal_override = Dog("Dog", "Cat")
animal_dog = Dog("Dog", "cat")

"""42. Animal → Cat տարբեր վարք
● override մեթոդ"""
class Animal(Animal):
    def sound(self):
        print("Some generic animal sound")
    def run(self):
        print("Running...")
class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")
    def run(self):
        print("Ihe dog is running away")

my_dog = Dog()
my_dog.sound()
my_dog.run()

"""43. Employee → Manager salary
● base salary + bonus"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.salary + self.bonus

emp = Employee("John", 1500)
mgr = Manager("Alice", 3000, 1000)
print(f"Employee {emp.name} Salary: ${emp.calculate_salary()}")
print(f"Manager {mgr.name} Total Pay: ${mgr.calculate_salary()}")


"""44. Shape → Rectangle area
● override area()"""
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.area = self.width * self.height

rectangle = Shape(100, 100)
print(f"Rectangle: {rectangle.width}")
print(f"Rectangle: {rectangle.height}")
print(f"Calculated Area: {rectangle.area()}")

"""45. Shape → Circle area
● օգտագործել π"""
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        #OVERRIDE
        return math.pi * self.radius ** 2

my_circle = Circle(10)
print(f"Circle: {my_circle.area()}")
print(f"Circle Area: {my_circle.area()}")

"""46. Vehicle → ElectricCar
● super() → init"""
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size

    def display_info(self):
        # Overriding
        print(f"{self.year} {self.brand} {self.model} with a {self.battery_size}kWh battery")

my_tesla = ElectricCar("Tesla", "Model S", 2024, 100)
my_tesla.display_info()

"""47. Vehicle → Bike override
● redefine method"""
class Vehicle:
    def __init__(self, car, model, year):
        self.car = car
        self.model = model
        self.year = year
    def move(self):
        print("Moving...")

class Bike(Vehicle):
    def __init__(self, model, year):
        super().__init__(model, year)

    def move(self):
        print("Driving...")

my_vehicle = Vehicle("Toyota", "Camry", 2022)
my_bike = Bike("Giant", "Escape 3", 2023)
my_vehicle.move()
my_bike.move()

"""48. Multi-level inheritance
A → B → C
● բոլոր init-ները կանչել super()-ով"""
class A:
    def __init__(self, model):
        self.model = model

class B(A):
    def __init__(self, b):
        super().__init__()
        self.b = b
class C(B):
    def __init__(self, c):
        super().__init__()
        self.c = c

"""49. Multiple inheritance (A, B → C)
● method resolution order տեսնել"""
class A:
    def __init__(self, model):
        self.model = model
class B:
    def __init__(self, b):
        super().__init__()
        self.b = b
class C(A,B):
    def __init__(self, c):
        super().__init__()
        self.c = c




































