#Array
lenguajes=['Java', 'Python', 'PHP', 'C#']

#Imprime todo el array
print(lenguajes)

#Imprime el primer elemento
print(lenguajes[0])

#Ordenar los elementos alfabéticamente
lenguajes.sort()
print(lenguajes)

#Imprime el primer elemento en la lista ordenada
print(lenguajes[0])

#Acceder a un elemento
aprendiendo=f'Estoy aprendiento {lenguajes[3]}'
print(aprendiendo)

#Modificación
lenguajes[2]='Kotlin'
print(lenguajes)

#Agregar elementos
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar un elemento
del lenguajes[1]
print(lenguajes)

#Eliminar el último elemento
lenguajes.pop()
print(lenguajes)

#Eliminar con POP
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('Kotlin')
print(lenguajes)