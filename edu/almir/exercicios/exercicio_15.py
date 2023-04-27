veto_a = []
pares = []
soma = 0
i = 0
for x in range(10):
    veto_a.append(int(input('digite um valor: ')))
maior = veto_a[0]
menor = veto_a[0]
for y in range(10):
    if veto_a[y] % 2 ==0:
        pares.append(veto_a[y])
print(f"Os números pares são {pares}")
for z in range(10):
    soma+= veto_a[z]
    media = soma / 10
    if veto_a[z] > media:
        i+=1
print(f"A quatidade acima da media são {i}")
for t in range(10):
    if maior < veto_a[t]:
        maior = veto_a[t]
    elif menor > veto_a[t]:
        menor = veto_a[t]
print(f"O maior numero é {maior} o menor é {menor}")