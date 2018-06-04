# --------------------- WEEK 2 --------------------- #
# --------------------- Lesson: Python Functions --------------------- #

# 1. Instructions

# 2. What is a function?
def sing_song():
    print("You may say I'm a dreamer")
    print("But I'm not the only one")
    print("I hope some day you'll join us")
    print("And the world will be as one")


sing_song()
sing_song()
sing_song()

# 3. Write a function
def loading_screen():
    print("This page is loading...")


loading_screen()

# 4. Whitespace
def about_this_computer():
  print("This computer is running on version Everest Puma")
print("This is your desktop")

about_this_computer()
about_this_computer()

# 5. Parameters
def mult_two_add_three(number):
    print(number * 2 + 3)


mult_two_add_three(0)

# 6. Multiple parameters
def mult_x_add_y(number, x, y):
  print(number*x + y)

mult_x_add_y(1, 3, 1)

# 7. Keyword arguments
def create_spreadsheet(title, row_count=1000):
  print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows")

create_spreadsheet("Applications", 10)

# 8. Returns
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age = calculate_age(2018, 1993)
dads_age = calculate_age(2018, 1953)

print("I am " + str(my_age) + " and my dad is " + str(dads_age) + " years old")

# 9. Multiple return values
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit

low, high = get_boundaries(100, 20)

print("Low limit: " + str(low) + " , high limit: " + str(high))

# 10. Scope
def calculate_age(birth_year):
  age = current_year - birth_year
  return age

current_year = 2018

print(current_year)

print(calculate_age(1970))

# 11. Review
def repeat_stuff(stuff, num_repeats=10):
    return (stuff * num_repeats)


lyrics = repeat_stuff("Row ", 3) + "Your Boat"

song = repeat_stuff(lyrics)

print(song)

# --------------------- Project: Physics Class --------------------- #

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = f_temp - 32 * 5/9
  return c_temp

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

def get_energy(mass, c = 3*10**8):
  return mass * (c*c)

bomb_energy = get_energy(bomb_mass)

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

# --------------------- Lesson: Syntax - Code Challenge --------------------- #

# 1. Introduction

# 2. Average
# Write your average function here:
def average(num1, num2):
  return (num1 + num2) / 2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# 3. Tenth Power
# Write your average function here:
def average(num1, num2):
  return (num1 + num2) / 2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# 4. Bond
# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# 5. Square Root
# Write your square_root function here:
def square_root(num):
  return num ** 0.5
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# 6. Tip
# Write your tip function here:
def tip(total, percentage):
  return total * percentage * 0.01
# Uncomment these function calls to test your tip function:
#print(tip(10, 25))
# should print 2.5
#print(tip(0, 100))
# should print 0.0

# 7. Win percentage
# Write your win_percentage function here:
def win_percentage(wins, losses):
  return wins / (wins + losses) * 100
# Uncomment these function calls to test your win_percentage function:
#print(win_percentage(5, 5))
# should print 50
#print(win_percentage(10, 0))
# should print 100

# 8. First Three Multiples
# Write your first_three_multiples function here:
def first_three_multiples(num):
  print(num)
  print(num*2)
  print(num*3)
  return num*3
# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# 9. Dog Years
# Write your dog_years function here:
def dog_years(name, age):
  age = age*7
  return(name + ", you are " + str(age) + " years old in dog years")

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# 10. Remainder
# Write your remainder function here:
def remainder(num1, num2):
  return (num1*2) % (num2/2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

# 11. All Operations
# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  a_plus_b = a + b
  print(a_plus_b)
  c_minus_d = c-d
  print(c_minus_d)
  first_times_second = a_plus_b * c_minus_d
  print(first_times_second)
  return(first_times_second % a)
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

# --------------------- Lesson: Control Flow --------------------- #

# 1. Introduction

# 2. Boolean Expressions
example_statement = "No"

statement_one = "Yes"

statement_two = "Yes"

statement_three = "No"

statement_four = "Yes"

# 3. Relation Operators: Equals and Not Equals
statement_one = True

statement_two = False

statement_three = True

# 4. Boolean variables
my_baby_bool = "true"
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two))

# 5. If statements
def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
    elif user_name == "angela_catlady_87":
        return "I know it is you Dave! Go away!"


# Enter a user name here, make sure to make it a string
user_name = "Floor"

print(dave_check(user_name))

# 6. Relational Operators II
def greater_than(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    elif x == y:
        return "These numbers are the same"


def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"

# 7. Boolean Operators: AND
statement_one = False

statement_two = True

def graduation_reqs(gpa, credits):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"

# 8. Boolean Operators: OR
statement_one = True

statement_two = True

def graduation_mailer(gpa, credits):
  if credits >= 120 or gpa >= 2.0:
    return True

# 9. Boolean Operators: NOT
statement_one = False

statement_two = True

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  elif gpa >= 2.0 and credits < 120:
    return "You do not have enough credits to graduate."
  elif gpa < 2.0 and credits >= 120:
    return "Your GPA is not high enough to graduate."

# 10. Else statements
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

# 11. Else if statements
def grade_converter(gpa):
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa >= 1.0:
    return "D"
  else:
    return "F"

# 12. Try and exept statements
def raises_value_error():
    try:
        raise ValueError
    except ValueError:
        print("You raised a ValueError!")


raises_value_error()

#13. Review
def applicant_selector(gpa, ps_score, ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  elif gpa >= 3.0 and ps_score >= 90:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."