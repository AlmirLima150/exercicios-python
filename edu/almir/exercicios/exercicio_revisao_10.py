eleitores = int(input("digite a quantidade total de eleitoras"))

votos_brancos = int(input("digite a quantidade de votos em branco"))
votos_nulos = int(input("digite a quantidade de votos nulos"))
votos_validos = int(input("digite a quantidade de validos"))

if votos_validos + votos_nulos+ votos_brancos > eleitores:
    print("Essa eleição teve fraude! Refaça.")

percent_branco = (votos_brancos/eleitores) * 100
percent_nulos = (votos_nulos/eleitores) * 100
percent_validos = (votos_validos/eleitores) * 100

print(f"A porcentagem de votos validos é {percent_validos} %\n"
      f"A porcentagem de votos em branco é {percent_branco} %\n"
      f"A porcentagem de votos nulos é {percent_nulos} %"
      )
