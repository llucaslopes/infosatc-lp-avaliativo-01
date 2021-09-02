comprimento = int(input("Qual o comprimento da parede: "))
altura = int(input("Qual a altura da parede: "))
area  = comprimento*altura
tinta = area /3.16
resultado = tinta * 107
print("A quantidade de latas {} e o preco final {} ".format(tinta,resultado))