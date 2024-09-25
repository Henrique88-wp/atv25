# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).


for a in range(5):
    a = int(input("coloque a nota do aluno"))
    if a>=7:
        print("Parabéns este aluno foi aprovado.")
    else:
        print("infelismente este aluno(a) não foi aprovado(a)")