vetor_a = []
i=0
for x in range (10):
    vetor_a.append(int(input("adicione um valor ao vetor: ")))
outro_valor = int(input("adicione mais um valor ao vetor: "))
for y in range(10):
    if outro_valor == vetor_a[y]:
        i+=1
print(i)

