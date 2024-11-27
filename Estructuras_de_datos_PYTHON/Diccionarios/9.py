inventario = {
    "Arroz": 50,
    "Harina": 10,
    "Azúcar": 30,
    "Sal": 5,
    "Pasta": 20,
    "Aceite": 8
}


mas_de_20=[nombre for nombre,valor in inventario.items() if valor>20]
menor=min(inventario, key=inventario.get)
total=sum(inventario.values())

print(mas_de_20)
print(menor)
print(total)

