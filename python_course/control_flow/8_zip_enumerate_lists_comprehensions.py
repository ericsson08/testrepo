#1 exercise

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

for label,x,y,z in zip(labels, x_coord, y_coord, z_coord):
    print("{},{},{},{}".format(label,x,y,z))


#2

heights = [10,20,30,40]
names = ["Pet","Cat","Jul","Esc"]

cast = dict(zip(names,heights))
print(cast)


#3 UNZIP TUPLES

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names,heights = zip(*cast)
print(names)
print(heights)



#4 TRANSPOSE WITH ZIP

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)



#LISTS COMPREHENSIONS

#1 exercise: EXTRACT NAMES

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = []

for name in names:
    first_names.append(name.split()[0].lower())
print(first_names)


#2 MULTIPLES OF 3

multiples_3 = []

for x in range(1, 21):
    multiples_3.append(x * 3)
print(multiples_3)

multiples_3 = [x * 3 for x in range(1,21)]
print(multiples_3)

#3 SCORED names

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }


passed = [name for name, score in scores.items() if score >= 65]
print(passed)


passed = []
for name, score in scores.items():
    if score >= 65:
        passed.append(name)

print(passed)
