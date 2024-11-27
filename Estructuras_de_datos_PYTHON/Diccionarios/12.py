x=int(input("tamaño: "))

calificaciones={}

for i in range(x):
    nombre=input("Estudiante:")
    calificacion=int(input("Nota:"))
    while calificacion<0 or calificacion>100:
        calificacion=int(input("Nota:"))

    calificaciones[nombre]=calificacion


mas_alta=max(calificaciones, key=calificaciones.get)
promedio=sum(calificaciones.values())/len(calificaciones)
aprobados=[nombre for nombre,valor in calificaciones.items() if valor>59]

print(calificaciones)
print(mas_alta)
print(promedio)
print(aprobados)


