import random
import time


print('='*30)
print('Iniciando o Game...'.center(30))
print('='*30)
time.sleep(0.5)

tentativas=0
numero_sorteado=random.randint(1,100)
chute = -1

while chute != numero_sorteado:
    try:
        chute=int(input('Digite o valor que você acredita ser o correto'))
        time.sleep(0.5)
        if chute <1 or chute>100:
            print(f'Valor {chute} fora dos padrões estipulados ,tente novamente.')
            continue
        tentativas+=1
        if chute<numero_sorteado:
            print('Você errou tente um valor maior.')
        elif chute>numero_sorteado:
            print('Você errou tente um valor menor.')
        else:
            print(f'Parabéns você acertou o numero sorteado era {numero_sorteado}')
            print(f'Você precisou de {tentativas} tentativa(s) para adivinhar.')
    except ValueError:
        print('Valor digitado invalido ou inexistente,tente novamente.')


