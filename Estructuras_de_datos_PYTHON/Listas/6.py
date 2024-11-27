calificaciones = [
    ("Juan", 85),
    ("María", 92),
    ("Carlos", 70),
    ("Lucía", 90),
    ("Pedro", 60)
]

mas_alta=max(calificaciones, key=lambda x:x[1])

mas_baja=min(calificaciones, key=lambda x:x[1])

promedio=sum(valor for nombre,valor in calificaciones)/len(calificaciones)

mayores_a_80=[nombre for nombre,valor in calificaciones if valor>=80]

print(mas_alta)
print(mas_baja)
print(mayores_a_80)

