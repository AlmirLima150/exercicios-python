def numero_primo(n):
    mult=0
    for count in range(2,n):
        if (n % count == 0):
            mult += 1
    if(mult==0):
        print("É primo")
    else:
        print('não é primo')

numero_primo(17)