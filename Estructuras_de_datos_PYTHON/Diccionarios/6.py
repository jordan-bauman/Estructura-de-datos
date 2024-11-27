precios = {
    "Manzanas": 3.5,
    "Plátanos": 1.2,
    "Peras": 4.0,
    "Naranjas": 2.8
}

compras = {
    "Manzanas": 2,
    "Plátanos": 5,
    "Peras": 1.5,
    "Naranjas": 3
}


nueva= {producto: precios[producto]*compras[producto] for producto in precios}

maximo=max(nueva, key=nueva.get)

total_a_pagar= sum(nueva.values())

print("cantidad a pagar por producto:", nueva)
print("El producto más caro es:", maximo)
print("El total a pagar es:", total_a_pagar)

