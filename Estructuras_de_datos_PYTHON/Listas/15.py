productos = [
    ("Cámara", 350, 15),
    ("Laptop", 800, 30),
    ("Smartphone", 600, 25),
    ("Auriculares", 120, 50),
    ("Teclado", 80, 40),
    ("Ratón", 50, 60)
]


stock_bajo=min(productos, key=lambda x:x[2])[0]

stock_alto=max(productos, key=lambda x:x[2])[0]

aux=[nombre for nombre,precio,stock in productos if stock>30]

superior_a_100=[nombre for nombre, precio,stock in productos if precio>100]

cantidad_stock_mayor_a_30=len(aux)

precio_promedio=sum(precio for nombre,precio,stock in productos)/len(productos)

print(stock_bajo)
print(stock_alto)
print(superior_a_100)
print(cantidad_stock_mayor_a_30)
print(precio_promedio)


