result = 0

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8} #dictionary
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas'] #list

for object, count in basket_items.items(): #add items method for dictionaries to get key,value
    if object in fruits:
        result += count
print("There are {} fruits".format(result))

#ERROOOR ITERATION PRINT: DEPENDE DONDE LO PONGO SALE X VECES

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))
