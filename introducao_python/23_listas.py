# nomes = ['Maiza', 'Thiago', 'Theodoro', 'Maria Izadora']
# print(type(nomes))
# print(nomes)
# print(nomes[0])
# print(nomes[3])
# print(nomes[4])  # Erro por que o index não existe na lista
# print(len(nomes))  # Retorna a quantidade de elementes existe dentro da lista
# nomes[3] = "Maria"
# print(nomes)

# nomes = []
# while True:
#     nome = input("Digite -1 para sair ou cadastre um nome: ")
#     if nome == "-1":
#         break
#
#     nomes.append(nome)
#
# print(nomes)

# Método para inserir elementos em qualquer posição da lista
# nomes = ['Maiza', 'Thiago', 'Theodoro', 'Maria Izadora']
# nomes.insert(2, 'Pedro')
# print(nomes)

# Método para remove o último valor da lista caso não seja informado o index a ser removido
# nomes = ['Maiza', 'Thiago', 'Theodoro', 'Maria Izadora']
# nomes.pop(1)
# nomes.pop()
# print(nomes)

# Método remove da lista o elemento informado. Remove apenas o primeiro elemento encontrado
# nomes = ['Maiza', 'Thiago', 'Thiago', 'Theodoro', 'Maria Izadora']
# nomes.remove('Thiago')
# print(nomes)

# Como descobrir o indice de um determinado elemento da lista
# nomes = ['Maiza', 'Thiago', 'Thiago', 'Theodoro', 'Maria Izadora']
# print(nomes.index('Theodoro'))

# Ordenar listas
# nomes = ['Thiago', 'Maiza', 'Theodoro', 'Maria Izadora']
# nomes.sort()  # Altera a lista original
# nomes.sort(reverse=True)  # Não altera a lista original
# sorted(nomes)
# nomes_ordenados = sorted(nomes, reverse=True)
# print(nomes)
