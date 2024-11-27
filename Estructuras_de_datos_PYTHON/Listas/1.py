calificaciones = [85, 92, 78, 88, 90, 75, 68]
mayores_al_promedio=[]

mas_alta=max(calificaciones)
mas_baja=min(calificaciones)
promedio=sum(calificaciones)/len(calificaciones)

for i in range(len(calificaciones)):
    if calificaciones[i]>promedio:
        mayores_al_promedio.append(calificaciones[i])
    
print(calificaciones)
print(mayores_al_promedio)
print(mas_alta)
print(mas_baja)
