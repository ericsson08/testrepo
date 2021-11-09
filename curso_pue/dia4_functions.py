
def sayHello(nombre):
    print("Hola",nombre)

print("Hola")
print("mundo!")

sayHello("Toni")
sayHello("Pepe")

def suma(x,y):
    return x+y
print("suma: ", suma(5,5))
print("suma: ", suma("5","5")) #concatenar
#print("suma: ", suma("5", 5)) #error

suma = "Esto es suma ahora"
print(suma)

#me puedo cargar funciones si hago del suma


add = suma
print(add(5,10))
print(add)


var = """hola ESTE ES EL TEXO MULTILINEA"""

print(var)

#print identificador print(sayHello)

""" yo puedo redefinir funcion suma"""

def suma(x,y):
    return x-y
print(suma)
print(add)



def fn1(x,y,z):
    print("x:",x,"y:",y,"z:",z)
fn1(3, "hola", True)

def fn1(x,y=1,z=2): #parametros por defecto
    print("x:",x,"y:",y,"z:",z)
fn1(4)
#si quiero modificar Z
fn1(4,z=5) #cuando hacemos esto, sin conocer el valor de y podemos modificar el de z // estamos dando valores a dosargumentos que son opcionales



fn1(4,1,5)

arr = [4,1,5]
fn1(arr[0], arr[1], arr[2])
fn1(*arr) #desecmpaquetado

arr2= [4,1]
fn1(*arr2)



def fn2(**kwargs): #creamos un diccionario
    print(kwargs)

fn2(x=1, y=20, z="hola", pepe="manolo")

* = args
** = kwargs (keyword)

def fn3(x,*y,z=20, **valores): #todo lo que ponga a continuacion de y se ira para y, hay que mencionar z.
    print("x:",x,"y:",y,"z:",z, "valores:", valores) #este doble asterisco tiene que se rel ultimo
fn3(4,5,6, z=10, nombre="pepe", dni="888888j")

#elemento obligatorio
#elemento multivaluado
#elemento nominal opcional
#elemento XXXX

dic = {"x":4, "y":1, "z":5}
fn1(4,1,5)
fn1(dic["x"], dic["y"], dic["z"])
fn1(**dic) #desecmpaquetado del dicionario fn1(x=4, y=1, z=5) utiliza la clave (es el nombre del argumento) y lo usa como elemento nominal


#porque ERROR esto de aqui abajo?
def fn4(*args): #admite elemento multivaluado kwargs
    print("N argumentos:", len(args), "args:" args)

arr1 = ["hola", 3, True]

fn4(arr1)
fn4(*arr1)


x,z,y = 4,5,6

def fn5():
    return 4, "hola"

res = fn5()
print(type(res), res) #esto retorna una tupla

x,saludo = fn5()
print(x, saludo) #propiedad de asignacion multiple: requerimiento: #variables coinciude que vamos a asignar coincide con la # de elementos que tenemps en la colección, ya sea una lista, una tupla o un set.


dic = {"x":4, "y":5, "z": 7}
#for key,value in dic.items():
for item in dic.items():
    #print(item)
    print(key,value)


#SECUENCIA DE FIBONACHI: IMPORTANTE, TÍPICO EJEMPLO DE EXAMEN, ENTENDER AMBAS VERSIONES

def fibI(n):
    #print("versión iterativa")
    a, b = 0,1
    for count in range(n):
        a, b = b, a+b
        #aux = a
        #a = b
        #b = aux + b
        print(a, end= ' ') #p r i n t a space
    print()
    return a

def fibR(n):
    #print("versión recursiva")
    if n<1:
        return 0
    elif n<=2:
        return 1
    else:
        return fibR(n-1) + fibR(n-2)

#fibR(3) => fibR(2) + fibR(1) => 1 + 1 => 2

print(fibI(10))
print(fibR(10))


#ELEMENTOS DE UNA FUNCIÓN:

def fn6(x):
    print(x)
    x = 10
    print(x)

x = 20
print(x)
fn6(x)
print(x)

#en caso de los mutables, si va a cambiar si hacemos cambios dentro de la función.

def fn7(arr):
    print("dentro:", arr)
    arr[0] = 20#cambio el valor del elemento, mutable, esto si se mantiene el cambio despues
    arr = [40, 80, 90]#cambios de psosicion de memoria, REASIGNANDO
    print("dentro: ", arr)

arr = [10, 20, 30]
print("fuera: ", arr)
fn7(arr)
print("fuera: ", arr)

*elementos posicionales
** elementos nominales


def fn8():
    x = 20
    yyyy = 10
    print(x,yyyy)
x = 10
fn8()

#global cobra sentido cuando queremos reasignar variables desde dentro de la funcion hacia fuera

def fn8():
    global x
    x = 20
    global yyyy
    yyyy = 10
    print(x,yyyy)
x = 10
fn8()
print(x,yyyy)


#iterador: conjunto de datos que podemos recorrer de inicio a fin con la funcion next
#iter convierte cualquier colección en algo iterable

i = iter([11,22,33])
next(i)

#alfina obtendre una excpecion "StopIteration". Es como el for. Para poder correr el for, necesitamos una colección iterable.


#funcion range(): produce una SECUENCIA
var = range(5)
print(type(var), var)

var = list(range(5))
print(type(var), var)

def fn9():
    for i in range(10):
        #return i #opción A:en la primera iteración ya salta, asi que saltara 0
        yield i #es un generador, puedo iterarlo, puedo llamar un metodo next para que me devuelva sus valores

print(fn9())

res = fn9()
print("next: ", res.__next__())
print("next: ", res.__next__())
print("next: ", res.__next__())
print("next: ", res.__next__())

for x in fn9(): #esto es como el método next
    print(x)


#Función enumerate: convertir una array en un elemento enumerado

arr = ["pepe", "maria", "juan"]
print(enumerate(arr)) #es un objeto, lo mismo que en el caso del yiel, yo puede operar.
for name in enumerate(arr):
    print(name)


arr = ["pepe", "maria", "juan"]
print(enumerate(arr)) #es un objeto, lo mismo que en el caso del yiel, yo puede operar.
for idx, name in enumerate(arr):
    print("indice:", idx, "name:",name)


#Función zip

nombres = ["pepe", "maria", "juan"]
apellidos = ["fernandez", "ericsson", "gutierrez"]
dni = ["asdaf", "sadass", "ñdlpds"]

for i in range(len(nombres)):
    print("nombre:", nombres[i], "apellido:", apellidos[i], "dni:", dni[i])



for val in zip(nombres,apellidos,dni):
    print(val)

for nombre, apellido, dni in zip(nombres, apellidos, dni):
    print("nombre:", nombres[i], "apellido:", apellidos[i], "dni:", dni[i])
