# Receba um número do usuário e mostre a tabuada desse número

i = 1
tabuada = int(input('Tabuada de qual número voce deseja ver? '))
while i <= 10:
    print(f'{tabuada} * {i}: {tabuada * (i)}')
    i = i + 1
