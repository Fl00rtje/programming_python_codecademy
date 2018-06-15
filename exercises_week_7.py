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