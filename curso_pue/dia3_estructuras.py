## while

i = 0
while i<10:
    print("i: ",i)
    if i ==5:
        i+=3
    i+=1

#EX 2

i = 0 #iteración
y = 1
while i<10 and y != 0:
    print("i: ",i)
    if i ==5:
        i+=3
        break
    i+=1 #para no quedarnos siempre en el mismo loop
else:
    print("Hemos terminado el while")


#EX3

flag = True
x = [2,3,4,0,9]
i=0
while i<len(x):
    if(x[i]==0):
        flag = False
        break
    i+=1
if (flag):
    print("mi array es correcto")



x = [2,3,4,0,9]
i=0
while i<len(x):
    if(x[i]==0):
        break
    i+=1 #si no ponemos esto, esto seria un loop infinito de manual
else:
    print("mi array es correcto")


###FOR loop
#diferencia entre while y for:

#con while puedo MODIFICAR
#on for # NOTE:  cuando queremos recorrer una colección fija

#EX4:
arr = [2,3,4,0,9]
for item in arr:
    print(item)#tengo que darle una colección, algo que sea iterable

#EX 5: Genera un iterador donde los valores empiezan en 0 y terminan en 5.
# eL LIMITE SUPERIOR NO SE INCLUYE?

# range (end) -> range (0, end, 1)
# range(start, end) -> range(start, end, 1)
# range(start, end, step) -> range(start,end,step)

for i in range(5):
    print("i",i)

#EX 6

for i in range(-5,2,2):
    if(i==-3):
        i = 5
    print("i:", i)

#en el for la secuencia es sagrada, no la puedo modificar.

#Una bandera es cualquier variable booleana, lo utilizamos como un marcados (por ejemplo, si es 0 o 1)

for x in range(5):
    fin = False
    for y in range(5):
        if(y==0):
            fin = True
            break
    if fin:
        break

texto = "hola"
for letra in texto:
    print(letra)



#ESTO ME DA ERROR POR QUE?
dic = {"clave1":"val1", "clave2":"valor2"}
print(dic.keys())
print(dic.values())
print(dic.items())

for item in dic.items():
    print("key: ", key,"value: ", value)

#break:
#continue:
#pass: no hace nada. Sirve como marcador. Recurso que existe y es palabra reservada, NO PUEDO NOMBRAR UNA VARIABLE.

if x==5:
    pass #cuando salte ya lo haré

if x==5:
    print("esto no puede ser")
else:
    pass

#EXERCISES

#OPCION 1

list = []
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        list.append(i)
print(list)

#OPCION 2

list = []
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        list.append(str(i))
print(",".join(list))


#OPCION 3

list = []
texto = ""
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        list.append(str(i))
        texto+=str(i)+","

print(",".join(list))
print(texto[:2])


#EXERCISE 2

#n = int(input("dame un numero: "))
n = 8
dictionary = {}


for x in range (1,n+1):
    dictionary[x] = x*x #importante el parentsis sino nos cargamos dictionary
    #dictionary.update({x: x*x}) syntaxi alternativa

print(dictionary)

#EXERCISE 3

n =["34,67,55,33,12,98"]
m = []


for i in n:
    m.append((i))

print(m)
print(tuple(m))

#CORRECCIÓN 3
n = "34,67,55,33,12,98"
s = n.split(',')
t = tuple(s)
print(t)
print(s)

#PREGUNTA 4


c=50
h=30
#n = input("introduce numeros separados por comas: ")
n = "100,150,180 "

res = []
lst = n.split(',')
import math
for value in lst:
    q = round((2*c*int(value))/h)**0.5)

    #q = math.sqrt((2*c*int(value))(h))
    res.append(q)
print(",".join(res))







n = 100,150,180



def square_root(C=50,n,H=30):
    for i in range(n+1):
    Q = (2 * C * D)/H
    result(D)
def


Q = Square root of [(2 * C * D)/H]
C = 50
H = 30
D = 100,150,180

for i in D:
    [(2 * C * D(i))/H]
    print(i)

#PREGUNTA 5

x = int(input("dame un numero: "))
y = int(input("dame otro: "))
x,y = 3,5

lst = [[], [], []]

for i in range(x):
    lst.append([])
    #lst[i] = []
    for j in range(y):
        # new = list()
        lst[i].append(i*j)
        #list[i][j] = i*j

print(lst)

#LIST COMPREHENSIONS

lst = [[i*j for j in range(y)]for i in range(x)]
print(lst)

lst = []
for i in range(5):
    lst.append(i**2)
lst =
print()

#PREGUNTA 6

n = without,hello,bag,world
Solution:
items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)




#PREGUNTA 7
texto =
arr = texto.split(" ")

texto = list(set(arr))

#esta seria la alternativa, usar la funcion sorted idirecemtane sobre el set
s = set(arr)
arr = sorted(s)

print(", ".join(arr))

#PREGUNTA 8

items = []
#num =
num = "0100,0011,1010,1001".split(",")
#num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    #if not x%5:
    if x%5 ==0:
        itemps.append(p)

print ','.join(items)
