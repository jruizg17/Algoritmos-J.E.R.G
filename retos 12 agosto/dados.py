import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

suma = dado1 + dado2

print("Dado 1:", dado1)
print("Dado 2:", dado2)
print("Suma:", suma)

if (dado1 == 1 and dado2 == 1):
    print("GANASTE")
elif suma == 3:
    print("GANASTE")
elif suma == 11:
    print("GANASTE")
elif (dado1 == 2 and dado2 == 2) or (dado1 == 6 and dado2 == 6):
    print("GANASTE")
elif suma == 7:
    print("GANASTE")
else:
    print("PERDISTE")