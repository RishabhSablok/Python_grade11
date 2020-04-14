# Conditionals 

user_val = int(input("Please enter a number: "))
num1 = 15

# Only one of the following condition will execute
# Basic if
if user_val > num1:
   print("Value is over 15")
# else if
elif user_val == num1:
    print("Value is 15")
# else has no condition
else:
   print("Value is under 15")


# Comparitive operator 
# >, <, >=, <=, ==
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal to sign


compare1 = 12 >= 13
# Compare1 is an boolean as you are comparing two numbers
print(compare1)
