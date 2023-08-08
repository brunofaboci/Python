import random


def jogar():
    mostrar_mensagem_boas_vindas()
    palavra_secreta = busca_palavra_secreta()
    letras_acertadas = ["_"] * len(palavra_secreta)
    # letras_acertadas = ["_" for letra in palavra_secreta] # forma alternativa
    print(letras_acertadas)
    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ").strip().lower()

        if chute in palavra_secreta:
            adiciona_letra_na_posicao_correta(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print("Você Venceu!")
    if enforcou:
        print("Você perdeu!")
    print("Fim de Jogo")


def mostrar_mensagem_boas_vindas():
    print("***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************")


def busca_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().lower())
    arquivo.close()

    return random.choice(palavras)


def adiciona_letra_na_posicao_correta(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


if __name__ == "__main__":
    jogar()
