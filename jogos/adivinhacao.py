import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Níveis de dificuldade: (1)Fácil (2)Médio (3)Difícil")
    dificuldade = int(input("Escolha  a dificuldade: "))

    total_de_tentativas = 20 if dificuldade == 1 else (10 if dificuldade == 2 else 5)

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if 100 < chute < 1:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if chute == numero_secreto:
            print("Você acertou!")
            print("Pontuação: {}".format(pontos))
            break
        else:
            if chute > numero_secreto:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif chute < numero_secreto:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do jogo")

if __name__ == "__main__":
    jogar()
