productos = [
    ("Cámara", 350, 15),
    ("Laptop", 800, 30),
    ("Smartphone", 600, 25),
    ("Auriculares", 120, 50),
    ("Teclado", 80, 40),
    ("Ratón", 50, 60)
]

mas_caro=max(productos, key=lambda x:x[1])[0]

mas_stock=max(productos, key=lambda x:x[2])[0]

precio_mayor_100=[nombre for nombre,precio,stock in productos if precio>100]

aux=[stock for nombre,precio,stock in productos if stock>20]

stock_mayor_a_20=len(aux)

print(mas_caro)
print(mas_stock)
print(precio_mayor_100)
print(stock_mayor_a_20)

