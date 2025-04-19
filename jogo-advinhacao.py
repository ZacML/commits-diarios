import random

print('Bem vindo ao jogo da adivinhação!!!')
print('Tente adivinhar o número de 1 a 100!')

print('')

palpite = 0
tentativas = 0
jogar_novamente = 'sim'
numero_sorteado = random.randint(1, 100)

while jogar_novamente == 'sim':
    palpite = int(input('Digite seu palpite: '))

    if palpite > 100 or palpite < 1:
        print('')
        print('Número inválido. Digite um número de 1 a 100')
        print('')
        continue
    else:
        tentativas += 1

        if palpite < numero_sorteado:
            print(f'O numero é maior que {palpite}. Tente novamente.')
            print('')
        elif palpite > numero_sorteado:
            print(f'O numero é menor que {palpite}. Tente novamente')
            print('')
        else:
            print(f'Parabéns! Você acertou o número em {tentativas} tentativas!')
            print('')
            jogar_novamente = input('Quer jogar novamente? (sim/nao): ').lower()

            if jogar_novamente == 'nao':
                print('Adeus')
                break
            else:
                print('\nBoa sorte!\n')
                numero_sorteado = random.randint(1, 100)
                tentativas = 0
                print('')
                continue
