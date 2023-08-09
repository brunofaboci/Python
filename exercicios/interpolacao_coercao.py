# 1- Crie uma string que interpole seu nome e idade.
nome = "Bruno"
idade = 34

print("meu nome é {} e tenho {} anos".format(nome, idade))

# 2- Escreva uma expressão com interpolação que calcule o dobro de um número.
num = 5
print("o dobro de {} é igual a {}".format(num, (num * 2)))

# 3- Faça uma interpolação que exiba o resultado da soma de dois números.
num1 = 9
num2 = 2
print("a soma entre {} e {} é igual a {}".format(num1, num2, (num1 + num2)))

# 4- Crie uma expressão de interpolação que calcule o produto de dois números.
print("o produto entre {} e {} é igual a {}".format(num1, num2, (num1 * num2)))

# 5- Escreva uma interpolação que mostre o resultado da subtração de dois números.
print("a diferença entre {} e {} é igual a {}".format(num1, num2, (num1 - num2)))

# 6- Interpole uma expressão que divida dois números e mostre o resultado.
print("a divisão entre {} e {} é igual a {}".format(num1, num2, (num1 / num2)))

# 7- Crie uma expressão de interpolação que eleve um número ao quadrado.
num = 5
print("a potência de {} é igual a {}".format(num, (num ** 2)))

# 8- Escreva uma interpolação que mostre o resto de uma divisão.
print("o resto da divisão entre {} e {} é igual a {}".format(num1, num2, (num1 % num2)))

# 9- Crie uma interpolação que converta um número inteiro em uma string.
num = 5
print("o numero {} era do tipo {}, mas agora é do tipo {}".format(num, type(num), type(str(num))))

# 10- Escreva uma expressão de interpolação que converta uma string em um número inteiro.
num_str = '5'
print("o numero {} era do tipo {}, mas agora é do tipo {}".format(num_str, type(num_str), type(int(num))))

# 11- Interpole uma expressão que converta um número de ponto flutuante em uma string
num = 5.0
print("o numero {} era do tipo {}, mas agora é do tipo {}".format(num, type(num), type(str(num))))

# 12- Crie uma interpolação que converta uma string em um número de ponto flutuante.
num_str = '5'
print("o numero {} era do tipo {}, mas agora é do tipo {}".format(num_str, type(num_str), type(float(num))))
