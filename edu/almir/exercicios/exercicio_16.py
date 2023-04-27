n = int(input("digite o tamanho dos vetores: "))

vetor_a = []
vetor_b = []
vetor_c = []

for x in range(n):
    vetor_a.append(int(input("adicione um valor no vetor A: ")))
    vetor_b.append(int(input("adicione um valor no vetor B: ")))

for y in range(n):
    vetor_c.append(vetor_a[y]+vetor_b[y])

print(vetor_a)
print(vetor_b)
print(vetor_c)