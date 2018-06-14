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

# --------------------- Lesson: String methods --------------------- #

# 1. Introduction

# 2. Formatting methods
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()

print(poem_author)
print(poem_author_fixed)

# 3. Splitting strings
line_one = "The sky has given over"

line_one_words = line_one.split()

# 4. Splitting strings II
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

author_names_seperate = [name.split() for name in author_names]
print(author_names_seperate)

author_last_names = []
for name in author_names_seperate:
    author_last_names.append(name[-1])

print(author_last_names)

# 5. Splitting strings III
spring_storm_text = \
"""The sky has given over
its bitterness.
Out of the dark change
all day long
rain falls and falls
as if it would never end.
Still the snow keeps
its hold on the ground.
But water, water
from a thousand runnels!
It collects swiftly,
dappled with black
cuts a way for itself
through green ice in the gutters.
Drop after drop it falls
from the withered grass-stems
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')

# 6. Joining strings
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)

# 7. Joining strings II
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

# 8. Strip()
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

# 9. Replace
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')

# 10. Find()
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')

# 11. Format()
def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet)

# 12. Format() II
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

# 13. Review
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

# print(highlighted_poems_stripped)

highlighted_poems_details = []
for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(':'))

print(highlighted_poems_details)

titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
    titles.append(poem[0])
    poets.append(poem[1])
    dates.append(poem[2])

for poem in highlighted_poems_details:
    print("The poem {title} was published by {poet} in {date}.".format(title=poem[0], poet=poem[1], date=poem[2]))

# --------------------- Project: Thread Shed --------------------- #

daily_sales_replaced = daily_sales.replace(';,;', '|')

daily_transactions = daily_sales_replaced.split(",")
# print(daily_transactions)

daily_transactions_split = []
for transaction in daily_transactions:
    daily_transactions_split.append(transaction.split("|"))

# print(daily_transactions_split)

transactions_clean = []
for transaction in daily_transactions_split:
    transaction_stripped = []
    for item in transaction:
        transaction_stripped.append(item.strip())
    transactions_clean.append(transaction_stripped)

print(transactions_clean)

customers = []
sales = []
thread_sold = []

for transaction in transactions_clean:
    customers.append(transaction[0])
    sales.append(transaction[1])
    thread_sold.append(transaction[2])

print(customers)
print(sales)
print(thread_sold)

total_sales = 0

for sale in sales:
    sale = float(sale.strip("$"))
    total_sales += sale

print(total_sales)

print(thread_sold)

thread_sold_split = []

for thread in thread_sold:
    if "&" not in thread:
        thread_sold_split.append(thread)
    else:
        thread_colors = thread.split("&")
        for color in thread_colors:
            thread_sold_split.append(color)


print(thread_sold_split)

def color_count(color):
    sum = 0
    for thread in thread_sold_split:
        if color == thread:
            sum += 1
    return sum


print(color_count('white'))

colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

for color in colors:
    print("We sold " + str(color_count(color)) + " threads of {} today".format(color))