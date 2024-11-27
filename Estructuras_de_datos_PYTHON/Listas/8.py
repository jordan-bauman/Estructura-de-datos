productos = [
    ("Laptop", 150, "Portátil con pantalla de 15 pulgadas"),
    ("Móvil", 250, "Smartphone de última generación"),
    ("Auriculares", 80, "Auriculares con cancelación de ruido"),
    ("Teclado", 120, "Teclado mecánico retroiluminado"),
    ("Ratón", 95, "Ratón inalámbrico ergonómico"),
    ("Monitor", 70, "Monitor Full HD de 24 pulgadas")
]

mas_caro=max(productos, key=lambda x:x[1])[0]

mas_barato=min(productos, key=lambda x:x[1])[0]

total=sum(valor for nombre,valor,description in productos)

entre_80_y_100=[nombre for nombre,valor,description in productos if valor>79 and valor<121]

print(mas_caro)
print(mas_barato)
print(total)
print(entre_80_y_100)



