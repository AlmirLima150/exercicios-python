import random
list_shakespeare = ['"É mais fácil obter o que se deseja com um sorriso do que à ponta da espada." - Willian Shakespeare', '"Não há arauto mais perfeito da alegria do que o silêncio. Eu sentir-me-ia muito pouco feliz se me fosse possível dizer a que ponto o sou." - Willian Shakespeare', '"Você faz suas escolhas e suas escolhas fazem você" - Willian Shakespeare']
list_socrates = ['"Só sei que nada sei" - Sócrates', '"Conhece-te a ti mesmo e conhecerás o universo e os deuses" - Sócrates', '"A vida irrefletida não vale a pena ser vivida" - Sócrates']
list_lispector = ['"Até cortar os próprios defeitos pode ser perigoso. Nunca se sabe qual é o defeito que sustenta nosso edifício inteiro." - Clarice Lispector', '"Renda-se, como eu me rendi. Mergulhe no que você não conhece como eu mergulhei. Não se preocupe em entender, viver ultrapassa qualquer entendimento." - Clarice Lispector', '"Sim, minha força está na solidão. Não tenho medo nem de chuvas tempestivas nem das grandes ventanias soltas, pois eu também sou o escuro da noite." - Clarice Lispector']
while True:
    escolha_o_autor = int(input(" [1] William Shakespeare\n [2] Sócrates\n [3] Clarice Lispector\n"))
    match escolha_o_autor:
        case 1:
            for x in range(1): 
                print(list_shakespeare[random.randrange(3)])
        case 2:
            for z in range(1):
                print(list_socrates[random.randrange(3)])
        case 3:
            for c in range(1):
                print(list_lispector[random.randrange(3)])

