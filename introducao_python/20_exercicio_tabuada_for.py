# Receba um numero e mostre a tabuada completa dele usando o laço FOr

numero = int(input('Informe o numero que deseja visualizar a tabuada: '))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
