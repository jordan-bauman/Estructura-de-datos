ventas = [
    ("Laptop", 150),
    ("Móvil", 250),
    ("Auriculares", 80),
    ("Teclado", 120),
    ("Ratón", 95),
    ("Monitor", 70)
]


mas_vendido=max(ventas, key=lambda x:x[1])[0]

total_vendidos=sum(valor for nombre,valor in ventas)

mayor_a_50=[nombre for nombre,valor in ventas if valor>50]

print(mas_vendido)
print(total_vendidos)
print(mayor_a_50)

