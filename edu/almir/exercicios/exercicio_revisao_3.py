# vetor = []
# for x in range(3):
#     vetor.append(int(input("Digite um numero ")))
# maior = vetor[0]
# for y in range(3):
#     if vetor[y] > maior:
#         maior = vetor[y]
# print(f"O maior numero é {maior}")

num1 = int(input("digite um numero "))
num2 = int(input("digite um numero "))
num3 = int(input("digite um numero "))

if num1 > num3 and num1 > num2:
    print(num1)
elif num2 > num3 and num2 > num1:
    print(num2)
else:
    print(num3)