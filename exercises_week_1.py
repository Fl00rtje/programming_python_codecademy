# 1. Change Codecademy to your name in the script to the right. Run the code to see what it does!
# As soon as you're ready, move on to the next exercise to begin learning to write your own Python programs!
my_name = "Floor"
print("Hello and welcome " + my_name + "!")

# 2. Documentation is an important step in programming. Write a comment describing the first program you want to write!
#We are going to check the weather! Or not. Who knows?

# 3. Print the distinguished greeting "Hello world!"
print("Hello world!")

# 4. Print your name using the print() command.
print('Floor')

# 5. Update the variable meal to reflect each meal of the day before we print it.
# We've defined the variable "meal" here to be breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "Salad with salmon"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "Potatoes and steak"

# Printing out dinner
print("Dinner:")
print(meal)

# 6. You might encounter a SyntaxError if you open a string with double quotes and end it with a single quote.
# Update the string so that it starts and ends with the same punctuation.
# You might encounter a NameError if you try to print a string but fail to put any quotes around it.
# Python expects the words of your string to be defined elsewhere but can't find where they're defined.
# Add quotes to either side of the string to squash this bug.
# Update the malformed strings in the workspace to all be strings.
print("This message has mismatched quote marks!")
print("This message has no quote marks!")

# 7.1 A recent movie-going experience has you excited to publish a review. You rush out of the cinema and hastily
# begin programming to create your movie-review website: The Big Screen's Greatest Scenes Decided By A Machine.
# Create the following variables and assign integer numbers to them: release_year and runtime.
release_year = 2018
runtime = 160

# 7.2 Now, create the variable rating_out_of_10 and assign it a float number between one and ten.
rating_out_of_10 = 7.5

# 8. Print out the result of this equation: 25 * 68 + 13 / 28
print(25 * 68 + 13 / 28)

# 9.1 You've decided to get into quilting! To calculate the number of squares you'll need for your first quilt
# let's create two variables: quilt_width and quilt_length.
# Let's make this first quilt 8 squares wide and 12 squares long.
# Print out the number of squares you'll need to create the quilt!
quilt_width = 8
quilt_length = 12

print(quilt_width * quilt_length)
# 9.2 It turns out that quilt required a little more material than you have on hand!
# Let's only make the quilt 8 squares long. How many squares will you need for this quilt instead?
quilt_width = 8
quilt_length = 8

print(quilt_width * quilt_length)

# 10.1 Using the exponent operator, print out how many squares you'll need for a 6x6 quilt, a 7x7 quilt, and an 8x8 quilt.
print(6 ** 2)
print(7 ** 2)
print(8 ** 2)

#10.2 Your 6x6 quilts have taken off so well, 6 people have each requested 6 quilts.
# Print out how many tiles you would need to make 6 quilts apiece for 6 people.
print(6 ** 2 * 6 ** 2)

# 11.1 You're trying to divide 16 people into 4 teams. The teams are Team 1, Team 2, Team 3, and Team 0.
# All of the people line up and count off from person 1 to person 16. Assign their teams by performing a modulo by 4
# on each person's number.
# In the program, we've created person1_team and person2_team.
# Assign the rest of the players to teams by taking their number and performing a modulo by 4.
person1_team = 1 % 4
person2_team = 2 % 4
# Add the rest of the teams here
person3_team = 3 % 4
person4_team = 4 % 4
person5_team = 5 % 4
person6_team = 6 % 4
person7_team = 7 % 4
person8_team = 8 % 4
person9_team = 9 % 4
person10_team = 10 % 4
person11_team = 11 % 4
person12_team = 12 % 4
person13_team = 13 % 4
person14_team = 14 % 4
person15_team = 15 % 4
person16_team = 16 % 4

# And here we'll print them out
print("Person 1 belongs to team:", person1_team)
print("Person 2 belongs to team:", person2_team)
print("Person 3 belongs to team:", person3_team)
print("Person 4 belongs to team:", person4_team)
print("Person 5 belongs to team:", person5_team)
print("Person 6 belongs to team:", person6_team)
print("Person 7 belongs to team:", person7_team)
print("Person 8 belongs to team:", person8_team)
print("Person 9 belongs to team:", person9_team)
print("Person 10 belongs to team:", person10_team)
print("Person 11 belongs to team:", person11_team)
print("Person 12 belongs to team:", person12_team)
print("Person 13 belongs to team:", person13_team)
print("Person 14 belongs to team:", person14_team)
print("Person 15 belongs to team:", person15_team)
print("Person 16 belongs to team:", person16_team)

# 12.1 Concatenate the strings and save the message they form in the variable message.
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

message = string1 + string2 + string3 + string4 + string5 + string6

# 13. We're doing a little bit of online shopping and find a pair of new sneakers.
# Right before we check out, we spot a nice sweater and some fun books we also want to purchase!
# Update the total_price to include the prices of nice_sweater and fun_books.
total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00

total_price += nice_sweater
total_price += fun_books

# 14. Assign the string "Stranger, if you passing meet me and desire to speak to me, why should you not speak to me?
# And why should I not speak to you?" to the variable to_you.
to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""

# 15. Create variables my_age, half_my_age, greeting, name, and greeting_with_name.
# Assign values to each using your knowledge of division and concatenation!

my_age = 34
half_my_age = my_age / 2
greeting = "Hi "
name = "Floor"
greeting_with_name = greeting + name

print(greeting_with_name)