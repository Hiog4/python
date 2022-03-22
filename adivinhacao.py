#adivinhação.py
import random

def jogar():
    print('**********************')
    print('Bem vindo ao jogo da adivinhação!')
    print('**********************')
    numero_secreto=random.randrange(1,101)
    total_tentativas=0
    pontos=1000

    print('Qual o nível de dificuldade?')
    print('(1)Fácil (2)Médio (3)Difícil')
    nivel=int(input('Defina o nível: '))

    if (nivel ==1):
        total_tentativas = 20
    elif(nivel==2):
        total_tentativas = 10
    else:
        total_tentativas = 5

        
    for tentativa in range(1,total_tentativas+1):
        print(f'Tentativa {tentativa} de {total_tentativas}')
        chute=int(input('Digite um número entre 1 e 100: '))
        if(chute==numero_secreto):
            print('Acertou!')
            break
        else:
            pontos_perdidos=abs(numero_secreto-chute)
            pontos=pontos-pontos_perdidos
            if(chute>numero_secreto):
                print('Errou! Seu número foi maior que o número secreto!')
            else:
                print('Errou! Seu número foi menor que o número secreto!')

    print('**Fim de jogo**')
    print(f'o número secreto era {numero_secreto}. Você fez {pontos} pontos')

if (__name__=='__main__'):
    jogar()