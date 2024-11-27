ventas = {
    "Laptop": 150,
    "Móvil": 250,
    "Auriculares": 80,
    "Teclado": 120,
    "Ratón": 95,
    "Monitor": 70
}


mas_de_100_ventas=[nombre for nombre,valor in ventas.items() if valor>100]
mas_vendido=max(ventas, key=ventas.get)
total_vendido=sum(ventas.values())

print(mas_de_100_ventas)
print(mas_vendido)
print(total_vendido)