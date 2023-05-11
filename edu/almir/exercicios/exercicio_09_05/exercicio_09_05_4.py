def achando_vogais(texto):
    VOGAIS = "AaEeIiOoUu"
    i = 0
    for x in texto:
        if x in VOGAIS:
            i+=1
    print(f"A quantidade de vogais no texto é {i}")

achando_vogais("O rato roeu a roupa do rei de Roma")
achando_vogais("Santa cruz é o maior clube do nordeste!")
