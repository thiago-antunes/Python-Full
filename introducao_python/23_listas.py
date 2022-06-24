# nomes = ['Maiza', 'Thiago', 'Theodoro', 'Maria Izadora']
# print(type(nomes))
# print(nomes)
# print(nomes[0])
# print(nomes[3])
# print(nomes[4])  # Erro por que o index não existe na lista
# print(len(nomes))  # Retorna a quantidade de elementes existe dentro da lista
# nomes[3] = "Maria"
# print(nomes)

nomes = []
while True:
    nome = input("Digite -1 para sair ou cadastre um nome: ")
    if nome == "-1":
        break

    nomes.append(nome)

print(nomes)
