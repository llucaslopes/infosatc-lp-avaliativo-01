valort = int(input("Qual o valor total "))
cofre= valort * 0.07
primeiro  = valort * 0.46
segundo = valort * 0.32
terceiro = valort - (cofre+primeiro+segundo)
print("O total do premio: {} quanto o cofre vai ganhar: {} quanto o premiero via ganhar: {} o segundo: {} e o terceiro: {} ".format(valort,cofre,primeiro,segundo,terceiro))