productos = [
    ("Laptop", 150),
    ("Móvil", 250),
    ("Auriculares", 80),
    ("Teclado", 120),
    ("Ratón", 95),
    ("Monitor", 70)
]

mas_barato=min(productos, key=lambda x:x[1])

mas_caro=max(productos, key=lambda x:x[1])

total=sum(valor for nombre,valor in productos)

mayores_a_100=[nombre for nombre,valor in productos if valor>100]

print(mas_barato)
print(mas_caro)
print(total)
print(mayores_a_100)

