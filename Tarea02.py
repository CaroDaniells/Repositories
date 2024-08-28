#Tarea 02

## Creación de un objeto range
r = range(1, 10)

## Mutabilidad: intentar modificar un elemento del range
### error
    r[0] = 5

## Suma de ranges
### error
r_sum = r + range(10, 20)

## Muktiplicación por un entero
### error
r_mult = r * 2

## Slicing
### Sí se puede
r_slice = r[2:5]
print(r_slice)

## Conversión a lista y a tupla
r_list = list(r)
r_tuple = tuple(r_list)

print('tupla:', r_tuple)
print('lista:', r_list)


