
# calculo de medias
notas = []  # lista para armazenar as notas

print("=== Registro de Notas da Turma ===")
qtd_alunos = int(input("Digite a quantidade de alunos: "))

for i in range(qtd_alunos):
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {i+1}: "))
            if nota < 0 or nota > 10:
                print("Erro: a nota deve estar entre 0 e 10.")
            else:
                notas.append(nota)
                break
        except ValueError:
            print("Erro: digite apenas números.")

# cálculo da média
media = sum(notas) / len(notas)

print("\n=== Resultado ===")
print(f"Notas registradas: {notas}")
print(f"Média da turma: {media:.2f}")
