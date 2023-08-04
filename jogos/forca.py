def jogar():
    print("***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ").strip().lower()
        index = 0

        for letra in palavra_secreta:
            if chute == letra:
                print("Letra {} encontrada na posição {}".format(letra, index))
            index += 1

    print("Fim de Jogo")


if __name__ == "__main__":
    jogar()
