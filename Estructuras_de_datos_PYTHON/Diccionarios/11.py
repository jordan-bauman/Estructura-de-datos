x=int(input("Ingrese el tamaño de la muestra:"))

productos={}

for i in range(x):
    clave=input("producto: ")
    valor=int(input("Precio: "))
    productos[clave]=valor


mas_alto=max(productos, key=productos.get)
total=sum(productos.values())


print(productos)
print(mas_alto)
print(total)



