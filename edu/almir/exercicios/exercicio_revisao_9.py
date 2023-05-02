idade_anos = int(input("digite quantos anos você tem ?"))
idade_mes = int(input("digite quantos anos você tem em meses?"))
idade_dias = int(input("digite quantos anos você tem dias?"))

idade_em_anos = idade_anos * 365
idade_em_mes = idade_mes * 30

print(f"Sua idade representada em dias é {idade_em_anos + idade_em_mes + idade_dias} dias")