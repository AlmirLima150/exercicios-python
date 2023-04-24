import random
list_shakespeare = ['"É mais fácil obter o que se deseja com um sorriso do que à ponta da espada." - Willian Shakespeare', 
'"Não há arauto mais perfeito da alegria do que o silêncio. Eu sentir-me-ia muito pouco feliz se me fosse possível dizer a que ponto o sou." - Willian Shakespeare', 
'"Você faz suas escolhas e suas escolhas fazem você" - Willian Shakespeare',
'"Todo mundo é capaz de dominar uma dor, exceto quem a sente." - Willian Shakespeare',
'"Lutar pelo amor é bom, mas alcançá-lo sem luta é melhor." - Willian Shakespeare',
'"Lamentar uma dor passada, no presente, é criar outra dor e sofrer novamente." - Willian Shakespeare',
'"A paixão aumenta em função dos obstáculos que se lhe opõem." - Willian Shakespeare',
'"Aceita o conselho dos outros, mas nunca desistas da tua própria opinião." - Willian Shakespeare',
'"O amor não se vê com os olhos mas com o coração." - Willian Shakespeare',
'"A alegria evita mil males e prolonga a vida." - Willian Shakespeare']
list_socrates = ['"Só sei que nada sei" - Sócrates', 
'"Conhece-te a ti mesmo e conhecerás o universo e os deuses" - Sócrates', 
'"A vida irrefletida não vale a pena ser vivida" - Sócrates',
'"A alegria evita mil males e prolonga a vida." - Sócrates',
'"Sábio é aquele que conhece os limites da própria ignorância." - Sócrates',
'"Deve-se temer mais o amor de uma mulher do que o ódio de um homem." - Sócrates',
'"Uma vida sem desafios não vale a pena ser vivida." - Sócrates',
'"Sob a direção de um forte general, não haverá jamais soldados fracos." - Sócrates',
'"A sabedoria começa na reflexão." - Sócrates',
'"O verdadeiro conhecimento vem de dentro." - Sócrates']
list_lispector = ['"Até cortar os próprios defeitos pode ser perigoso. Nunca se sabe qual é o defeito que sustenta nosso edifício inteiro." - Clarice Lispector', 
'"Renda-se, como eu me rendi. Mergulhe no que você não conhece como eu mergulhei. Não se preocupe em entender, viver ultrapassa qualquer entendimento." - Clarice Lispector', 
'"Sim, minha força está na solidão. Não tenho medo nem de chuvas tempestivas nem das grandes ventanias soltas, pois eu também sou o escuro da noite." - Clarice Lispector',
'"Que ninguém se engane, só se consegue a simplicidade através de muito trabalho." - Clarice Lispector',
'"A palavra é meu domínio sobre o mundo." - Clarice Lispector',
'"Não quero ter a terrível limitação de quem vive apenas do que é passível de fazer sentido. Eu não: quero é uma verdade inventada." - Clarice Lispector',
'"Ela acreditava em anjo e, porque acreditava, eles existiam." - Clarice Lispector',
'"E, se você me achar esquisita, respeite também. Até eu fui obrigada a me respeitar." - Clarice Lispector',
'"Passei a vida tentando corrigir os erros que cometi na minha ânsia de acertar." - Clarice Lispector',
'"Eu não sou tão triste assim, é que hoje eu estou cansada." - Clarice Lispector']
while True:
    escolha_o_autor = int(input(" [1] William Shakespeare\n [2] Sócrates\n [3] Clarice Lispector\n"))
    match escolha_o_autor:
        case 1:
            for x in range(1): 
                print(list_shakespeare[random.randrange(10)])
        case 2:
            for z in range(1):
                print(list_socrates[random.randrange(10)])
        case 3:
            for c in range(1):
                print(list_lispector[random.randrange(10)])
