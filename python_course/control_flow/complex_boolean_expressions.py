# Examples of bolean expressions

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")

#Bad examples

#1. Don't use True or False as conditions

if True:
    print("This indented code will always get run.")

# Another bad example. Allways will be run.
if is_cold or not is_cold:
    print("This indented code will always get run.")

#2. Be careful writing expressions that use logical operators (2n one is a string)

if weather == "snow" or "rain":
    print("Wear boots!")

#3. Don't compare a boolean variable with == True or == False

# Bad example
if is_cold == True:
    print("The weather is cold!")

# Good example
if is_cold:
    print("The weather is cold!")


#Truth Value Testing

'''Here are most of the built-in objects that are considered False in Python:'''

- constants defined to be false: None and False
- zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
- empty sequences and collections: '"", (), [], {}, set(), range(0)



Exercicse

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)
