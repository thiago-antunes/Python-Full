# Receba 4 notas de um aluno e exiba se ele foi aprovado
# (nota maior ou igual que 6)
# Se ele ficou de recuperação (nota maior ou igual a 4) ou se ele foi
# reprovado (nota menor do que 4)

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 6:
    print(f'Aluno aprovado com média {media}')
elif media >= 4:
    print(f'Aluno em recuperação com média {media}')
else:
    print(f'Aluno reprovado com média {media}')
