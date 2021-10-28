#Question 3

#x = input("Escribe tu numero aquí: ")

x = "34,67,55,33,12,98"

y = x.split(",")

z = tuple(y)

print(y)
print(z)


#Question 4

# Q = Square root of [(2 * C * D)/H]

C = 50
H = 30
D = "100,150,180"

D = D.split(",")
E = []

#Q = [(2 * C * D)/H]**0.5

for d in D:
    q = round(((2 * C * int(d))/H)**0.5) #convertir el valor en int
    E.append(int(q))

print(E)

#Question 5

X = "3,5"
Y = X.split(",")
lst = []

for y in range(int(Y[0])): #3 veces
    aux = []
    for i in range (int(Y[1])): #5 veces
        print(i,y)
        aux.append(i*y)
    print(aux)
    lst.append(aux)
print(lst)


print(Y)
print(Z)
