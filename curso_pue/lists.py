arr


# no podemos comprar cosas que no son comparables

arr3 = ["4", "0", 1]

# no podemos sumar arrays

#operadores

arr4 = [3,4]*4
print(arr4)
print(len(arr4))

del arr3 # esto elimina la referencia, al acceder nos daria nameerror


#append y #extend

arr3.append("jjj")
arr4 = ["3","aaa"]
arr3.extend(arr4)

#sorted (function) #sort(method)

soted no modifica la lista de forma interna
sort si modifica y retorna none (methond)

#TUPLAS: una vez creada no podemos modificar sucontenido pero si podemos operar con ella.


#DICCIONARIOS: SON MUTABLES: ACCEDER, MODIFICAR ETC

dic = {"hola": "hello", "3": "tres"}

#para acceder a keys

dic.keys()
dic.values()
dic.items()

#SET: Nos permite tener valores no duplicades.

#La estructura es con llaves, la diferencia es que no tiene valores. Y eso hace que esos elemenos no sean repetibles

s = {"asd", "pepe", "asd", "111"}

s1 = sorted(s)
