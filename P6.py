class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

las_pintas = ("Corazón", "Trébol", "Diamante", "Pica")

import random
carta  = (random.randint(1,13))
if (carta == 11):
    valor = "J"
elif (carta == 12):
    valor = "Q"
elif (carta == 13):
    valor = "K"
else: 
    valor = carta
pinta = random.choice(las_pintas)
carta_ejemplo = Carta(valor,pinta)

print("Valor:", carta_ejemplo.valor)
print("Pinta:", carta_ejemplo.pinta)
