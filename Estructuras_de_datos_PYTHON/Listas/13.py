productos = [
    ("Cámara", 350, 4.5),
    ("Laptop", 800, 4.8),
    ("Smartphone", 600, 4.2),
    ("Auriculares", 120, 3.9),
    ("Teclado", 80, 4.0),
    ("Ratón", 50, 4.3)
]


mas_bajo=min(productos, key=lambda x:x[1])[0]

mas_alto=max(productos, key=lambda x:x[1])[0]

calificacion_mayor_a_3=[cali for nombre,precio,cali in productos if cali>=4]

mayor_a_100=[precio for nombre,precio,cali in productos if precio>100]

superior_a_100=len(mayor_a_100)

print(mas_alto)
print(mas_bajo)
print(calificacion_mayor_a_3)
print(superior_a_100)


