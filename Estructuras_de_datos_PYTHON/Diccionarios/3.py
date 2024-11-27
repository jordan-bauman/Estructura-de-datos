#calificaciones
calificaciones={
    "Ana":90,
    "Pedro":56,
    "Maria":34,
    "Carlos":55,
    "Berta":33,
    "Mario":73
}






#creamos lista con aprobados
aprobados=[nombre for nombre,nota in calificaciones.items() if nota>=60]

#creamos lista con reprobados
reprobados=[nombre for nombre,nota in calificaciones.items() if nota<60]

print(aprobados)
print(reprobados)
