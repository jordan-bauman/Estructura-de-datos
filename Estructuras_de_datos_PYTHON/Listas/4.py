estudiantes = [
    ("Juan", 85),
    ("María", 92),
    ("Carlos", 78),
    ("Lucía", 95),
    ("Pedro", 70)
]


mas_alta=max(estudiantes, key=lambda x:x[1])

mas_baja=min(estudiantes, key=lambda x:x[1])

promedio=sum(valor for nombre,valor in estudiantes)/len(estudiantes)

aprobados=[nombre for nombre,valor in estudiantes if valor>=80]

print(mas_alta)
print(mas_baja)
print(promedio)
print(aprobados)


