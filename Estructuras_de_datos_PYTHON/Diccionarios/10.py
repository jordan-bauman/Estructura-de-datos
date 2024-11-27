estudiantes = {
    "Sofía": 85,
    "Miguel": 92,
    "Andrés": 45,
    "Lucía": 77,
    "Carla": 58,
    "Pedro": 60,
    "Laura": 90
}

aprobados=[nombre for nombre, valor in estudiantes.items() if valor>59]
mas_alta=max(estudiantes, key=estudiantes.get)
promedio= sum(estudiantes.values())/len(estudiantes)

print(aprobados)
print(mas_alta)
print(promedio)

