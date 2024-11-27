calificaciones = {
    "Juan": {"Matemáticas": 85, "Historia": 78, "Inglés": 92},
    "María": {"Matemáticas": 88, "Historia": 82, "Inglés": 79},
    "Carlos": {"Matemáticas": 58, "Historia": 70, "Inglés": 65},
    "Lucía": {"Matemáticas": 95, "Historia": 90, "Inglés": 91},
    "Pedro": {"Matemáticas": 70, "Historia": 75, "Inglés": 68}
}


promedios={}

for estudiante,materias in calificaciones.items():
    promedio=sum(materias.values())/len(materias)
    promedios[estudiante]=promedio

print(promedios)

