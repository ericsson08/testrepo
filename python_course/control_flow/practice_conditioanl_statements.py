'''Practice: Which prize'''

points = 174

if points <= 50:
    result = ('Oh! You got a wooden_rabbit prize')
if points <= 150:
    result = ('Oh! You got a no prize')
elif points <= 180:
    result = ('Oh! You got a wafer_thin_mint prize')
else:
    result = ('Congrats! You got a penguin_prize prize')

print(result)


'''Guess my number'''

hidden_number = 8
guess_number = 7

if guess_number > hidden_number:
    result = ("You are too high")
elif guess_number < hidden_number:
    result = ("You are too low")
else:
    result = ('Thats the right number')

print (result)

'''Tax Purchase'''

state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)
