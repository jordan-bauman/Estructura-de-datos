#creamos diccionarios
conjunto={
    "juan":56,
    "Pedro":78,
    "Maria":67,
    "Antonia":67,
    "Ana":98,
    "Brandon":99
}


#promedio de calificaciones
promedio=sum(conjunto.values())/len(conjunto)


#la nota más alta
alta=max(conjunto,key=conjunto.get)


#calificaciones mayores a 60
aprobados= sum(1 for i in conjunto.values() if i>=60)


#mostramos
print(f"Promedio: {promedio}\n La nota más alta: {alta}\n aprobados: {aprobados}")



