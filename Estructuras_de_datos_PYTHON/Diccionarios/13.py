print("----Bienvenido al sistema----")
print("Ingrese la cantidad de productos:")
x=int(input())

productos={}

for i in range(x):
    nombre=input("Producto: ")
    valor=int(input("Cantidad disponible: "))

    while valor<0:
        print("No puede haber cantidad negativa, intente de nuevo:")
        valor=int(input("Cantidad disponible: "))

    productos[nombre]=valor

mayor_cantidad=max(productos, key=productos.get)
menor_cantidad=min(productos, key=productos.get)
cantidad_total=sum(productos.values())

print(" ")
print("Productos registrados: ")
print(productos)
print(" ")
print("Producto con la mayor cantidad en el inventario:")
print(mayor_cantidad)
print(" ")
print("Producto con la menor cantidad en el inventario:")
print(menor_cantidad)
print(" ")
print("Cantidad total de productos:")
print(cantidad_total)


