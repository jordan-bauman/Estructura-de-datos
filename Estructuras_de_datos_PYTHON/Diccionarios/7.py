inventario = {
    "Camisetas": 15,
    "Pantalones": 8,
    "Zapatos": 20,
    "Sombreros": 5,
    "Chaquetas": 12,
    "Bufandas": 30
}

productos_mayor_a_diez=[nombre for nombre,valor in inventario.items() if valor>10]

menor=min(inventario, key=inventario.get)

total=sum(inventario.values())

print(productos_mayor_a_diez)
print(menor)
print(total)