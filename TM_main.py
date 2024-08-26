# Tarea de MODELOS para el 26 de Agosto
# https://docs.python.org/3/tutorial/datastructures.html

from collections import deque

## 5.1 More on Lists []
print('MORE ON LISTS')
animales = ['lobo', 'pingüino', 'orangután', 'león', 'ballena', 'caballo', 'león']

print('Lista de animales:', animales)
print('Número de leones en la lista:', animales.count('león'))
print('El pingüino está en la posición:', animales.index('pingüino'))
print('El segundo león está en la posición:', animales.index('león', 4))
animales.reverse()
print('La lista de animales, al revés, es:', animales)
animales.append('bisonte')
print('Agregando un nuevo animal:', animales)
animales.sort()
print('La lista de animales en orden alfabético:', animales)
animales.pop(2)
print('Quité al caballo:', animales)

### Using Lists as Stacks

print('\n\n')
print('Using Lists as Stacks')

stack = [3, 7, 11, 91, 22]

print('Stack:', stack)
stack.append(8)
print('Agregando un número:', stack)
stack.append(15)
print('De nuevo agregando un número:', stack)
print('Regrésame el último valor agregado:', stack.pop())
print('Logré sacarlo de la lista:', stack)
print('Regrésame el penúltimo valor agregado:', stack.pop())
print('Lo saqué de la lista:', stack)

### Using Lists as Queues

print('\n\n')
print('Using Lists as Queues')

fiesta = ['Saúl', 'Alex', 'Sara', 'Caín', 'Nim']

print('Los que vinieron a la fiesta:', fiesta)
fiesta.append('Marisol')
fiesta.append('Enzo')
print('Llegaron más a la fiesta:', fiesta)
print('El primero que llegó fue:', fiesta.pop(0))
print('Ya se fue, ahora quedan:', fiesta)

### List Comprehensions

print('\n\n')
print('List Comprehensions')

cubos = []
for x in range(10):
    cubos.append(x**3)

print('Lista de potencias al cubo:', cubos)

### Nested List Comprehensions

print('\n\n')
print('Nested List Comprehensions')

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print('Matriz:', matriz)
matrix_t = [[row[i] + 10 for row in matriz] for i in range(3)]
print('Agregué 10 a cada valor:', matrix_t)

print('Cambio el formato:')
for row in matrix_t:
    print(row)
    print("\n")

## The del statement

print('\n\n')
print('THE DEL STATEMENT')

muebles = ['silla', 'puerta', 'escritorio', 'cama', 'sillón']
print('Lista de muebles:', muebles)
del muebles[0]
print('quité la silla:', muebles)

## Tuples and Sequences

print('\n\n')
print('TUPLES AND SEQUENCES')

tupla = (10, 'texto', [1, 2, 3])

print("Primer elemento:", tupla[0])
print("Segundo elemento:", tupla[1])

anidada = (tupla, (4, 5))
print("Tupla anidada:", anidada)

try:
    tupla[0] = 20
except TypeError as e:
    print("Error al modificar:", e)

x, y, z = (7, 'hola', [4, 5])
print("x:", x)
print("y:", y)
print("z:", z)

print("Tupla vacía:", ())
print("Tupla con un elemento:", (42,))

## Sets

print('\n\n')
print('SETS')

colores = {'rojo', 'verde', 'azul', 'rojo', 'amarillo', 'verde'}

print("Conjunto de colores:", colores)

print("'azul' está en colores?", 'azul' in colores)
print("'rosa' está en colores?", 'rosa' in colores)

colores_frescos = {'rojo', 'amarillo', 'blanco'}
colores_primavera = {'verde', 'amarillo', 'azul'}

print("Colores frescos pero no en primavera:", colores_frescos - colores_primavera)

print("Colores en frescos o primavera:", colores_frescos | colores_primavera)

print("Colores en ambos conjuntos:", colores_frescos & colores_primavera)

print("Colores en uno pero no en ambos:", colores_frescos ^ colores_primavera)

colores_unicos = {color for color in colores if color not in colores_frescos}
print("Colores únicos en el conjunto original:", colores_unicos)


## Dictionaries

print('\n\n')
print('DICTIONARIES')

comida = {
    'pizza': 'italiana',
    'sushi': 'japonesa',
    'tacos': 'mexicana'
}

print("Categoría de 'pizza':", comida['pizza'])

comida['croissant'] = 'francesa'
print("Diccionario actualizado:", comida)

del comida['sushi']
print("Eliminar 'sushi':", comida)

print("Tipos de comida en el diccionario:", list(comida))

print("'tacos' está en el diccionario?", 'tacos' in comida)
print("'sushi' está en el diccionario?", 'sushi' in comida)

comida2 = dict(burger='americana', curry='india')
print("Nuevo diccionario de comida:", comida2)

longitudes = {platillo: len(platillo) for platillo in comida}
print("Longitudes de los nombres de comida:", longitudes)


## Looping Techniques

print('\n\n')
print('LOOPING TECHNIQUES')

paises_capitales = {
    'Japón': 'Tokio',
    'Canadá': 'Ottawa',
    'Francia': 'París',
    'México': 'Ciudad de México'
}

print("Países y sus capitales:")
for pais, capital in paises_capitales.items():
    print(pais, capital)

paises = ['Japón', 'Canadá', 'Francia', 'México']
capitales = ['Tokio', 'Ottawa', 'París', 'Ciudad de México']

print("\nPaíses y sus capitales emparejados:")
for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}.")

print("\nPaíses en orden inverso:")
for pais in reversed(paises):
    print(pais)

print("\nPaíses en orden alfabético:")
for pais in sorted(paises):
    print(pais)

paises_con_repetidos = ['Japón', 'Canadá', 'Japón', 'Francia', 'México', 'Canadá']
print("\nPaíses únicos en orden alfabético:")
for pais in sorted(set(paises_con_repetidos)):
    print(pais)

datos_paises = ['Japón', None, 'Francia', 'México', None]
paises_filtrados = [pais for pais in datos_paises if pais is not None]
print("\nPaíses filtrados:", paises_filtrados)

## MORE ON CONDITIONS

print('\n\n')
print('MORE ON CONDITIONS')

papeleria = ['cuaderno', 'lápiz', 'borrador', 'bolígrafo', 'carpeta']

objeto = 'lápiz'
if objeto in papeleria:
    print(f"El {objeto} está en la lista de papelería.")
else:
    print(f"El {objeto} no está en la lista de papelería.")

objeto1 = 'cuaderno'
objeto2 = 'cuaderno'
if objeto1 is objeto2:
    print(f"{objeto1} y {objeto2} son el mismo objeto.")
else:
    print(f"{objeto1} y {objeto2} son diferentes objetos.")

item1 = 'lápiz'
item2 = 'bolígrafo'
if item1 != item2 and len(item1) < len(item2):
    print(f"{item1} es diferente de {item2} y es más corto.")
else:
    print(f"{item1} es igual a {item2} o es más largo.")

papeleria_completa = True
falta_item = False
if papeleria_completa and not falta_item:
    print("La lista de papelería está completa y no falta ningún ítem.")
else:
    print("La lista de papelería no está completa o falta algún ítem.")

item1, item2, item3 = '', 'cuaderno', 'bolígrafo'
primer_item_disponible = item1 or item2 or item3
print(f"El primer ítem disponible es: {primer_item_disponible}")

items = ['lápiz', 'bolígrafo', 'cuaderno']
if (count := len(items)) > 2:
    print(f"Hay {count} ítems en la lista de papelería.")


print('\n\n')
print('COMPARING SEQUENCES AND OTHER TYPES')

t1 = ('manzana', 'plátano', 'cereza')
t2 = ('manzana', 'plátano', 'dátil')
print(t1 < t2)

l1 = ['kiwi', 'mango', 'naranja']
l2 = ['kiwi', 'mango', 'pera']
print(l1 < l2)

print('apple' < 'banana' < 'cherry')

t3 = ('manzana', 'plátano', 'cereza', 'datil')
t4 = ('manzana', 'plátano', 'cereza')
print(t4 < t3)

print(('manzana', 5) < ('manzana', 7))

try:
    print('manzana' < 5)
except TypeError as e:
    print(e)

print(('manzana', 'plátano', ('cereza', 'datil')) < ('manzana', 'plátano', ('cereza', 'fig'), 4))
