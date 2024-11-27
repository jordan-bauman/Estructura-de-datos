productos={
    "Acciones": 45,
    "Bonos_10A": 340,
    "Bonos_5A": 40,
    "Bonos_2A": 30,
    "ETFs": 768
}

#lista con los que vendieron más de 50 unidades
lista=[activos for activos,valores in productos.items() if valores>50]

#el más vendido
vendido=max(productos, key=productos.get)

#cantidad total de ventas
vendidos=[valores for activos, valores in productos.items()]
total=sum(vendidos)

print(lista)
print(vendido)
print(total)
