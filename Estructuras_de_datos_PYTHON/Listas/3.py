edades = [17, 21, 18, 19, 22, 15, 16, 20, 18, 25]

edad_mas_baja=min(edades)

edad_mas_alta=max(edades)

promedio=sum(edades)/len(edades)

mayores_de_edad=[valor for valor in edades if valor>=18]

print(edad_mas_baja)
print(edad_mas_alta)
print(promedio)
print(mayores_de_edad)

