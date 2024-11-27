productos = [
    ("Cámara", 350),
    ("Laptop", 800),
    ("Smartphone", 600),
    ("Auriculares", 120),
    ("Teclado", 80),
    ("Ratón", 50)
]

mas_bajo=min(productos, key=lambda x:x[1])[0]

mas_alto=max(productos, key=lambda x:x[1])[0]

total=sum(valor for nombre,valor in productos)

mayores_a_100=[nombre for nombre, valor in productos if valor>100]

print(mas_bajo)
print(mas_alto)
print(total)
print(mayores_a_100)

