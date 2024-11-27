x=int(input("Cantidad de candidatos: "))

candidatos={}

for i in range(x):
    nombre=input("Candidato: ")
    valor=int(input(f"Votos obtenidos por {nombre}: "))
    candidatos[nombre]=valor


votos_emitidos=sum(candidatos.values())
ganador=max(candidatos, key=candidatos.get)
porcentajes={candidato: round((votos/votos_emitidos)*100,2) for candidato, votos in candidatos.items()}

print("\n--- Resultados ---")
print(f"Total de votos emitidos: {votos_emitidos}")
print(f"Candidato con más votos: {ganador} ({candidatos[ganador]} votos)")
print("\nPorcentajes por candidato:")
for candidato, porcentaje in porcentajes.items():
    print(f"{candidato}: {porcentaje}%")