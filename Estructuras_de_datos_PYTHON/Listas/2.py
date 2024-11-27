#lista con tuplas que contienen el nombre y el precio
productos = [
    ("Laptop", 150),
    ("Móvil", 250),
    ("Auriculares", 80),
    ("Teclado", 120),
    ("Ratón", 95),
    ("Monitor", 70)
]

#lista con los nombres de los productos con precio mayor a 50
mayor_a_50=[nombre for nombre,valores in productos if valores>50]

#variable con el precio mas alto
mas_caro=max(productos, key=lambda x:x[1])

#variable con el precio mas bajo
mas_barato= min(productos, key=lambda x:x[1])

#iteramos las tuplas de la lista para sacar la suma de sus valores
total=sum(valor for nombre,valor in productos)

#mostramos
print(mayor_a_50)
print(mas_caro)
print(mas_barato)
print(total)



