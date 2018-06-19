# --------------------- WEEK 7 --------------------- #

# --------------------- Lesson: Creating Dictionaries --------------------- #

# 1. What is a dictionary?
sensors =  {"pantry": 22, "living room": 21, "kitchen": 23, "bedroom": 20}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

# 2. Make a dictionary
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

# 3. Invalid Keys
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

# 4. Empty Dictionary
my_empty_dictionary = {}

# 5. Add a Key
animals_in_zoo = {}

animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

# 6. Add multiple keys
animals_in_zoo = {}

animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

# 7. Overwrite Values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight"

# 8. List comprehensions to dictionaries
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}

# 9. Review
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs, playcounts)}

print(plays)
plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

# --------------------- Lesson: Using Dictionaries --------------------- #

# 1. Using Dictionaries

# 2. Get a Key
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# 3. Get an invalid key
zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"])

# 4. Try/Exept to get a key
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level['matcha'] = 30

try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")

# 5. Safely get a key
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# 6. Delete a key
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items, health_points)

# 7. Get all keys
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

# 8. Get all values
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercise in num_exercises.values():
  total_exercises += exercise

print(total_exercises)

# 9. Get all items
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for function, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + str(function) + "s.")

# 10. Review
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your " + str(key) + " is the " + str(value) + " card.")

# --------------------- Project: Scrabble --------------------- #

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zipped_letters = zip(letters, points)
letter_to_points = {key: value for key, value in zipped_letters}
letter_to_points[" "] = 0

print(letter_to_points)

def score_word(word):
    point_total = 0
    for letter in word:
        if letter in word:
            point_total += letter_to_points[letter]
        else:
            point_total += 0
    return point_total


brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)

# --------------------- Lesson: Dictionaries - Code Challenge --------------------- #

# 1. Introduction

# 2. Sum Values
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value
  return sum

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# 3. Even keys
def sum_even_keys(my_dictionary):
    sum = 0
    for key, value in my_dictionary.items():
        if key % 2 == 0:
            sum += value
    return sum

print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6

# 4. Add ten
def add_ten(my_dictionary):
  for key, value in my_dictionary.items():
    my_dictionary[key] = value + 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# 5. Values that are keys
def values_that_are_keys(my_dictionary):
  values_keys = []
  for key in my_dictionary.keys():
    for value in my_dictionary.values():
      if key == value:
        values_keys.append(value)
  return values_keys

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# 6. Largest value
def max_key(my_dictionary):
  max_value = 0
  max_key = 0
  for key, value in my_dictionary.items():
    if value > max_value:
      max_value = value
      max_key = key
  return max_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
print(max_key({"Floor": 100, "Jaap": 75, "Pieter": 87}))

# 7. Word length dict
def word_length_dictionary(words):
  word_length = {}
  for word in words:
    word_length[word] = len(word)
  return word_length

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# 8. Frequency count
def frequency_dictionary(words):
  word_frequency = {}
  for word in words:
    word_frequency[word] = words.count(word)
  return word_frequency

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# 9. Unique values
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value in seen_values:
      continue
    else:
      seen_values.append(value)
  return len(seen_values)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# 10. Count first letter
def count_first_letter(names):
  letter_people = {}
  for key, value in names.items():
    first_letter = key[0]
    if first_letter in letter_people:
      letter_people[first_letter] += len(value)
    else:
      letter_people[key[0]] = len(value)
  return letter_people

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

