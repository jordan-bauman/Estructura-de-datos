estudiantes = [
    ("Juan", 85),
    ("María", 92),
    ("Carlos", 70),
    ("Lucía", 50),
    ("Pedro", 60)
]

mas_alta=max(estudiantes, key=lambda x:x[1])[0]

mas_baja=min(estudiantes, key=lambda x:x[1])[0]

promedio=sum(valor for nombre,valor in estudiantes)/len(estudiantes)

aprobados=[nombre for nombre,valor in estudiantes if valor>=60]

reprobados=[nombre for nombre,valor in estudiantes if valor<60]

print(mas_alta)
print(mas_baja)
print(promedio)
print(aprobados)
print(reprobados)


