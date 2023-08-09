# 1- Crie um programa que verifique se um número é positivo,
# negativo ou zero usando a estrutura condicional if.elsif.else.
import datetime

num = 5
if num > 0:
    print("numero positivo")
elif num < 0:
    print("numero negativo")
else:
    print("zero")

# 2- Implemente um programa que verifique se um número é par ou ímpar usando a estrutura condicional if.else.
num = 8
if num % 2 == 0:
    print("numero par")
else:
    print("numero impar")

# 3- Faça um programa que verifique se um número é divisível por 3 e 5 usando a estrutura condicional if.else.
num = 30
if num % 3 == 0 and num % 5 == 0:
    print("é divisível por 3 e 5")
else:
    print("não atende as condições")

# 4- Crie um programa que exiba "Bom dia" se a hora atual for menor que 12 e "Boa tarde" caso contrário,
# utilizando a estrutura condicional if.else.
# DICA: usar o método Time do ruby
current_time = datetime.datetime.now().time().hour
if 12 < current_time < 18:
    print("Boa tarde")
elif current_time > 18:
    print("Boa noite")
else:
    print("Bom dia")

# 6- Faça um programa que verifique se um número é múltiplo de 2, 3 ou 5
# utilizando a estrutura condicional if.elsif.else.
num = 30
if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
    print("é múltiplo de 2, 3 ou 5")
else:
    print("não atende as condições")

# 7- Implemente um programa que verifique se um número é maior que 10 e par,
# menor que 20 e ímpar ou qualquer outro caso utilizando a estrutura condicional.
num = 14
if num > 10 and num % 2 == 0:
    print("é maior que dez e par")
elif num < 20 and num % 2 != 0:
    print("é menor que 20 e impar")
else:
    print("não atende as condições")

# 8- Verifique se um número está entre 10 e 20 usando operadores logicos.
num = 11
print(10 < num < 20)

# 21- Escreva um programa que solicite ao usuário seu nome e idade.
# Verifique se o valor informado na idade é do tipo Integer, caso sim, prossiga,
# caso não, encerre o programa. Em seguida, exiba uma mensagem de boas-vindas
# que inclua o nome do usuário e seu grupo etário, utilizando condicionais if-elsif-else.
name = str(input("enter your name: "))
while True:
    try:
        age = int(input("enter your age: "))
        break
    except ValueError:
        print("invalid enter. please, enter a valid information")

print("hello {}! your age is {}".format(name, age))

# 22- Implemente um programa que solicite ao usuário uma temperatura em graus Celsius e converta-a para Fahrenheit.
# Utilize a fórmula de conversão e exiba o resultado com interpolação de strings.
while True:
    try:
        celsius = float(input("enter a temperature in celsius degrees: "))
        break
    except ValueError:
        print("invalid enter. please, enter a valid information")

fahrenheit = (celsius * (9 / 5)) + 32
print("{} celsius degrees is equivalent to {} fahrenheit".format(celsius, fahrenheit))
