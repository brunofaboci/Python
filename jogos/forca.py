def jogar():
    print("***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ").strip().lower()
        index = 0

        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)

    print("Fim de Jogo")


if __name__ == "__main__":
    jogar()
