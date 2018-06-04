# --------------------- WEEK 3 --------------------- #
# --------------------- Project: Sal's Shipping --------------------- #

def ground_shipping(weight):
    if weight < 2:
        cost = 20 + 1.5 * weight
    elif 2 <= weight < 6:
        cost = 20 + 3 * weight
        return cost
    elif 6 < weight <= 10:
        cost = 20 + 4 * weight
        return cost
    else:
        cost = 20 + 4.75 * weight
        return cost


print(ground_shipping(8.4))

premium_ground_shipping = 125


def drone_shipping(weight):
    if weight < 2:
        cost = 4.5 * weight
        return cost
    elif 2 <= weight < 6:
        cost = 9 * weight
        return cost
    elif 6 < weight <= 10:
        cost = 12 * weight
        return cost
    else:
        cost = 14.25 * weight
        return cost


print(drone_shipping(1.5))


def preferred_shipping(weight):
    if drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping:
        return "Drone shipping is cheapest for you. It's: " + str(drone_shipping(weight))
    elif ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:
        return "Ground shipping is cheapest for you. It's: " + str(ground_shipping(weight))
    else:
        return "Premium Ground Shipping is cheapest for you. Ground shipping costs: " + str(
            ground_shipping(weight)) + " Drone shipping costs: " + str(
            drone_shipping(weight)) + " Premium ground shipping costs: " + str(premium_ground_shipping)


print(preferred_shipping(4.8))
print(preferred_shipping(41.5))

# --------------------- Lesson: Control Flow - Code Challenge --------------------- #

# 1. Introduction

# 2. In Range
def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False


# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

# 3. Movie Review
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif 5 < rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

# 4. Twice as Large
def twice_as_large(num1, num2):
  if num1 > num2 * 2:
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

# 5. Power
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

# 6. Divisible by Ten
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

# 7. Max Number
def max_num(num1, num2, num3):
  if num1 == num2 and max(num1, num2, num3) == num1:
    return "It's a tie!"
  elif num1 == num3 and max(num1, num2, num3) == num1:
    return "It's a tie!"
  elif num2 == num3 and max(num1, num2, num3) == num2:
    return "It's a tie!"
  else:
  	return max(num1, num2, num3)
# Uncomment these function calls to test your in_range function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

# 8. Over Budget
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget < food_bill + electricity_bill + internet_bill + rent:
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# 9. Always False
def always_false(num):
  if num <= 0 or num > 0:
    return False
# Uncomment these function calls to test your in_range function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

# 10. Not Equal
def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False

# 11. Same Name
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False