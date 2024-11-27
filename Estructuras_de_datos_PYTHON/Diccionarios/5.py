biblioteca = {
    "1984": 10,
    "Don Quijote": 3,
    "El Principito": 5,
    "Cien Años de Soledad": 7,
    "Hamlet": 2,
    "La Odisea": 12
}

menos_de_cinco_copias=[nombre for nombre,copias in biblioteca.items() if copias<5]

mayor_cantidad_de_copias=max(biblioteca, key=biblioteca.get)

total_de_libros=sum(biblioteca.values())

print(menos_de_cinco_copias)
print(mayor_cantidad_de_copias)
print(total_de_libros)
