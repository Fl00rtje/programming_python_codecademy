# --------------------- WEEK 8 --------------------- #

# --------------------- Lesson: Classes --------------------- #

# 1. Types
print(type(5))

my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))

# 2. Class
class Facade:
  pass

# 3. Instantiation
class Facade:
  pass

facade_1 = Facade()

# 4. Object Oriented Programming (OOP)
class Facade:
  pass

facade_1 = Facade()

facade_1_type = type(facade_1)
print(facade_1_type)

# 5. Class variables
class Grade:
  minimum_passing = 65

# 6. Methods
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

# 7. Methods with arguments
class Circle:
    pi = 3.14

    def area(self, radius):
        area = self.pi * radius ** 2
        return area


circle = Circle()

pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)

# 8. Constructors
class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print('New circle with diameter: {}'.format(diameter))


teaching_table = Circle(36)

# 9. Instance Variables
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# 10. Attribute Functions
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for item in how_many_s:
  try:
    how_many_s.count
    number = item.count("s")
    print(number)
  except AttributeError:
    print("This element has no attribute count")

# 11. Self
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter * 0.5

    def circumference(self):
        circumference = 2 * self.pi * self.radius
        return circumference


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# 12. Everything is an object
print(dir(5))

def this_function_is_an_object(test):
  pass

print(dir(this_function_is_an_object))

# 13. String representation
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

# 14. Review
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))

# --------------------- Lesson: Inheritance and Polymorphism --------------------- #

# 1. Inheritance
class Bin:
  pass

class RecyclingBin(Bin):
  pass

# 2. Exceptions
class OutOfStock(Exception):
    pass


# Update the class below to raise OutOfStock
class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] < 1:
            raise OutOfStock
        self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
candle_shop.buy('green')

# 3. Overriding Methods
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text


class User:
    def __init__(self, username):
        self.username = username

    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text


class Admin(User):
    def edit_message(self, message, new_text):
        message.sender == True
        message.text = new_text

# 4. Super()
class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40

# 5. Interfaces
class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .00005

# 6. Polymorphism
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))
print(len(a_dict))
print(len(a_string))

# 7. Dunder methods I
class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine

# 8. Dunder Methods II
class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers

    def __len__(self):
        return len(self.lawyers)

    def __contains__(self, lawyer):
        return lawyer in self.lawyers


d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

# 9. Review
class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()