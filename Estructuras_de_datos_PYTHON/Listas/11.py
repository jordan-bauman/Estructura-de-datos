productos_vendidos = [
    ("Laptop", 10),
    ("Móvil", 25),
    ("Auriculares", 15),
    ("Teclado", 40),
    ("Ratón", 30),
    ("Monitor", 20)
]


mas_vendido=max(productos_vendidos, key=lambda x:x[1])[0]

menos_vendido=min(productos_vendidos, key=lambda x:x[1])[0]

mas_de_20=[nombre for nombre,valor in productos_vendidos if valor>20]

print(mas_de_20)
print(menos_vendido)
print(mas_vendido)


