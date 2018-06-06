# --------------------- WEEK 4 --------------------- #
# --------------------- Lesson: Python Lists --------------------- #

# 1. What is a list?
heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]

# 2. Lists II
heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]

# 3. List of lists
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]

ages = [['Aaron', 15], ['Dhruti', 16]]

# 4. Zip
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
print(list(names_and_dogs_names))

# 5. Empty lists
my_empty_list = []

# 6. Growing a list: append
orders = ['daisies', 'periwinkle']
print(orders)

orders.append('tulips')
orders.append('roses')
print(orders)

# 7. Growing a list: Plus (+)
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

new_orders = orders + ['lilac', 'iris']

broken_prices = [5, 3, 4, 5, 4] + [4]

# 8. Range I
list1 = range(9)
range1 = range(8)

# 9. Range II
list1 = range(5, 15, 3)
list2 = range(0, 40, 5)

# 10. Review
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

age = []
age.append(42)

all_ages = age + [32, 41, 29]
name_and_age = zip(first_names, all_ages)

ids = range(4)

# --------------------- Project: Python Gradebook --------------------- #

subjects = ["physics", "calculus", "poetry", "history"]
subjects.append("computer science")

grades = [98, 97, 85, 88]
grades.append(100)

gradebook = zip(subjects, grades)
gradebook = list(gradebook)
gradebook.append(("visual arts", 93))

print(gradebook)

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)

# --------------------- Lesson: Python Lists II --------------------- #

# 1. Operations on Lists

# 2. Length of a list
list1 = range(2, 20, 3)

list1_len = len(list1)
print(list1_len)

# 3. Selecting List Elements I
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

index4 = employees[4]
print(len(employees))

# This will generate an error because the list has 7 elements only.
print(employees[8])

# 4. Selecting List Elements II
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

print(len(shopping_list))

last_element = shopping_list[-1]
element5 = shopping_list[5]

print(last_element)
print(element5)

# 5. Slicing lists
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
print(beginning)

middle = suitcase[2:4]

# 6. Slicing lists II
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

start = suitcase[:3]
end = suitcase[-2:]

# 7. Counting elements in a list
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)

jake_votes = votes.count('Jake')
print(str(jake_votes) + " votes for Jake")
laurie_votes = votes.count('Laurie')
print(str(laurie_votes) + " votes for Laurie")
cassie_votes = votes.count('Cassie')
print(str(cassie_votes) + " votes for Cassie")

# 8. Sorting Lists I
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()
print(addresses)

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
print(cities)

# 9. Sorting Lists II
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
print(games)

games_sorted = sorted(games)
print(games_sorted)

# 10. Review
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]

twin_beds = inventory.count('twin bed')

inventory.sort()

# --------------------- Project: Len's Slice --------------------- #

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizzas = zip(prices, toppings)
pizzas = list(pizzas)
print(list(pizzas))

pizzas = sorted(pizzas)
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)