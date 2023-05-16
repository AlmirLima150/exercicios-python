def qnt_letras(texto):
    # i = 0
    # for x in texto:
    #     if x != ' ':
    #         i += 1
    # print(f'A quantidade de letras é {i}')
    # for y in range(len(texto - 1, - 1, - 1)):
    #     print(texto[y], end="")
    print(texto[::-1])
    print(len(texto) - texto.count(' '))

exemplo = qnt_letras('sara e muito amigavel')

