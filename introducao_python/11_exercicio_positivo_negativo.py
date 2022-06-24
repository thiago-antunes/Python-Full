# Receba um número e exiba se ele é positivo ou negativo.

numero = float(input('Informe um número: '))
if numero > 0:
    print(f'O número {numero} é positivo.')
elif numero < 0:
    print(f'O número {numero} é negativo.')
else:
    print(f'O número {numero} é 0 ou não é um número.')
