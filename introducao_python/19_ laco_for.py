# Percorre de 1 em 1
# for i in range(0, 100):
#    print(i)

# Percorre de 2 em 2
# for i in range(0, 100, 2):
#    print(i)


# Percorre de 1 em 1 em ordem decrescente
# for i in range(100, 0, -1):
#    print(i)


# Percorre de 2 em 2 em ordem decrescente
# for i in range(100, 0, -2):
#    print(i)


# Complexidade algoritmica (aninhamento)
k = 0
for i in range(0, 100):
    for j in range(0, 100):
        print(f"i= {i} j= {j}")
        k += 1

print(k)
