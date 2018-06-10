# --------------------- WEEK 5 --------------------- #

# --------------------- Lesson: Code Challenge --------------------- #

# 1. Introduction

# 2. Double Index
def double_index(lst, index):
  if index<= len(lst) - 1:
    new_list = lst[index] * 2
    return new_list
  else:
    return lst

print(double_index([3, 8, -10, 12], 4))

# 3. Remove Middle
def remove_middle(lst, start, end):
  lst_start = lst[:start]
  lst_end = lst[end+1:]
  lst = lst_start + lst_end
  return lst

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# 4. More than n
def more_than_n(lst, item, n):
  if n < lst.count(item):
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 6))

# 5. More frequent item
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item2) > lst.count(item1):
    return item2
  else:
    return item1

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# 6. Middle item
def middle_element(lst):
  if len(lst) % 2 != 0:
    middle_number = (len(lst) - 1) / 2
    return lst[int(middle_number)]
  else:
    below_middle = lst[int(len(lst) / 2) - 1]
    above_middle = lst[int(len(lst) / 2)]
    average = (below_middle + above_middle) / 2
    return average

print(middle_element([5, 2, -10, -4, 4, 5]))

# 7. Append sum
def append_sum(lst):
  new_element1 = lst[-1] + lst[-2]
  lst.append(new_element1)
  new_element2 = lst[-1] + lst[-2]
  lst.append(new_element2)
  new_element3 = lst[-1] + lst[-2]
  lst.append(new_element3)
  return lst

print(append_sum([1, 1, 2]))

# 8. Larger list
def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst2) > len(lst1):
    return lst2[-1]
  else:
    return lst1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# 9. Combine sort
def combine_sort(lst1, lst2):
  new_list_sorted = sorted(lst1 + lst2)
  return new_list_sorted

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# 10. Append size
def append_size(lst):
    length_list = list(range(1, len(lst) + 1))
    new_list = lst + length_list
    return new_list

print(append_size([23, 42, 108, 320, 2, 3, 4]))

# 11. Every three nums
def every_three_nums(start):
  if start > 101:
    return []
  else:
    return list(range(start, 101, 3))

print(every_three_nums(91))

# --------------------- Lesson: Python Loops --------------------- #

# 1. Introduction
dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)

# 2. Creat a for loop
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
    print(game)

for sport in sport_games:
    print(sport)

# 3. Using range in loops
promise = "I will not chew gum in class"

for i in range(5):
  print(promise)

# 4. Infinite loops
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)

# 5. Break
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for breed in dog_breeds_available_for_adoption:
  print(breed)
  if breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

# 6. Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)

# 7. While loops
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)

print(students_in_poetry)

# 8. Nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for scoop in location:
    scoops_sold += scoop

print(scoops_sold)

# 9. List comprehension
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

# 10. More list comprehensions
celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [ temperature * 9/5 + 32 for temperature in celsius]

print(fahrenheit)

# 11. Review
single_digits = range(10)
squares = []

for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)

print(squares)

cubes = [digit ** 3 for digit in single_digits]

print(cubes)

# --------------------- Project: Carly's Clippers --------------------- #

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 1]

total = 2 * 30 + 3 * 25 + 5 * 40 + 8 * 20 + 4 * 20 + 4 * 35 + 6 * + 2 * 50 + 1 * 35

print(total)

total_price = 0
for price in prices:
    total_price += price

average_price = total_price / len(prices)
print(total_price)
print("Average Price: " + str(average_price))

# list comprehension
new_prices = [price - 5 for price in prices]

# normal for loop
new_price = []
for price in prices:
    new_price.append(price - 5)

print(new_prices)
print(new_price)

total_revenue = 0

# i = []
# for number in range(len(hairstyles)):
#	i.append(number)

# for number in i:
#  total_revenue += prices[number] * last_week[number]

# improved version:
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30_solution1 = [price for price in new_prices if price < 30]

print(cuts_under_30_solution1)

cuts_under_30_solution2 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30_solution2)

# --------------------- Lesson: Code Challenge --------------------- #

# 1. Introduction

# 2. Divisible by 10
def divisible_by_ten(nums):
    divisible_by_10 = [num for num in nums if num % 10 == 0]
    return len(divisible_by_10)

print(divisible_by_ten([20, 25, 30, 35, 40]))

# 3. Greetings
def add_greetings(names):
  greeting = ["Hello, " + name for name in names]
  return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))

# 4. Delete starting even numbers
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# 5. Odd indices
def odd_indices(lst):
    empty_list = []
    for i in range(len(lst)):
        if i % 2 != 0:
            empty_list.append(lst[i])
    return empty_list


# REFACTORED

def odd_indices(lst):
    new_list = [lst[i] for i in range(len(lst)) if i % 2 != 0]
    return new_list


# OR

def odd_indices(lst):
    new_list = [lst[i] for i in range(1, len(lst), 2)]
    return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

# 6. Exponents
def exponents(bases, powers):
  exponents = []
  for base in bases:
    for i in range(len(powers)):
      exponents.append(base**powers[i])
  return exponents

print(exponents([2, 3, 4], [1, 2, 3]))

# 7. Larger sum
def larger_sum(lst1, lst2):
  if sum(lst1) > sum(lst2):
    return lst1
  elif sum(lst2) > sum(lst1):
    return lst2
  else:
    return lst1

print(larger_sum([1, 9, 5], [2, 3, 7]))

# 8. Over 9000
def over_nine_thousand(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
        if sum > 9000:
            return sum
            break
    return sum

print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([8000, 900]))
print(over_nine_thousand([]))

# 9. Max num
def max_num(nums):
  return max(nums)

def max_num(nums):
  maximum = 0
  for i in range(len(nums)):
    if nums[i] > maximum:
      maximum = nums[i]
  return maximum

print(max_num([50, -10, 0, 75, 20]))

# 10. Same values
def same_values(lst1, lst2):
    new_list = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            new_list.append(i)
    return new_list

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# 11. Reversed list
def reversed_list(lst1, lst2):
  lst2 = list(reversed(lst2))
  for i in lst2:
    if lst1[i] != lst2[i]:
      return False
    elif lst1 == [] and lst2 == []:
      return True
    else:
      return True


print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
print(reversed_list([1,3], [3,1]))