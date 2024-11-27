estudiantes = [
    ("Juan", {"Matemáticas": 85, "Historia": 78, "Inglés": 92}),
    ("María", {"Matemáticas": 88, "Historia": 82, "Inglés": 79}),
    ("Carlos", {"Matemáticas": 58, "Historia": 70, "Inglés": 65}),
    ("Lucía", {"Matemáticas": 95, "Historia": 90, "Inglés": 91}),
    ("Pedro", {"Matemáticas": 70, "Historia": 75, "Inglés": 68})
]

mas_en_math = max(estudiantes, key=lambda x: x[1]["Matemáticas"])[0]

mas_baja_historia= min(estudiantes, key=lambda x:x[1]["Historia"])[0]

promedio_ingles=sum(x[1]["Inglés"] for x in estudiantes)/len(estudiantes)

aprobados_math=[nombre for nombre,valor in estudiantes if valor["Matemáticas"] >=60]

aprobados_historia=[nombre for nombre,valor in estudiantes if valor["Historia"]>=60]





print(mas_en_math)
print(mas_baja_historia)
print(promedio_ingles)
print(aprobados_historia)
print(aprobados_math)
