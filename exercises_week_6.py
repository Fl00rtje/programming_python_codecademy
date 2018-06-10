# --------------------- WEEK 6 --------------------- #

# --------------------- Lesson: Introduction to Strings --------------------- #

# 1. Introduction
favorite_word = "cat"
print(favorite_word)

# 2. They're all lists!
my_name = "Floor"
first_initial = my_name[0]

# 3. Cut me a slice of string
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

# 4. Concatenating strings
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)

# 5. More and More String Slicing (How Long is that String?)
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  password = first_name[-3:] + last_name[-3:]
  return password

temp_password = password_generator(first_name, last_name)

print(temp_password)

# 6. Negative indices
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2:]
print(second_to_last)

final_word = company_motto[-4:]
print(final_word)

# 7. Strings are immutable
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]

# 8. Escape characters
password = "theycallme\"crazy\"91"

# 9. Iterating through strings
def get_length(string):
  for letter in string:
    return len(string)

print(get_length("test"))

# 10. Strings and conditions (part 1)
def letter_check(word, letter):
    for character in word:
        if character == letter:
            return True
    return False


print(letter_check("floor", "o"))

# 11. Strings and conditions (part 2)
def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:
  	return False

def common_letters(string_one, string_two):
  new_list = []
  for letter in string_one:
    if (letter in string_two) and not (letter in new_list):
      new_list.append(letter)
  return new_list

print(common_letters("floor", "borg"))

# 12. Review
def username_generator(first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[0:4]
  return username

def password_generator(username):
  password = ""
  for letter in range(0, len(username)):
    password += username[letter-1]
  return password