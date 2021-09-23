
#1 number to find the factorial of
number = 6
# track the current number being multiplied
current = 1
# start with our product equal to one: we set = 1 if dont, result = 0
product = 1


while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)


#FOR LOOP


# number we'll find the factorial of
# start with our product equal to one: we set = 1 if dont, result = 0
product = 1

# calculate factorial of number with a for loop
for i in range(2, 7):
    product *= i

# print the factorial of number
print(product)




#2COUNT BY CHECK

start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)



#3 FIRST ATTEMPT ERRRORRRRRRR

limit = 40

nearest_square = num**2

num = 1

while nearest_square < limit:

    num += 1

print(nearest_square)

#FINAL ATTEMPT

limit = 40

num = 0
while (num+1)**2 < limit:  #POR QUE NO num = 1 y ponemos en el loop "num"
    num += 1
nearest_square = num**2

print(nearest_square)


#Chek for undestanding

#1st ATTEMPT

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0


while count_odd < 5: #AQUÍ PUSE EL IF PERO CON UN AND Y SIN IF
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1 #Por que en esta posición y no dentro del loop????? FALLAN CONCEPTOS DE ITERACION



print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))
