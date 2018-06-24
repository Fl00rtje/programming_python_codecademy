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