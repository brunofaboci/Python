import forca
import adivinhacao

print("****************")
print("***Bem vindo!***")
print("****************")

print("(1) Adivinhação (2) Forca")
jogo = int(input("Escolha um jogo: "))

adivinhacao.jogar() if jogo == 1 else forca.jogar()
