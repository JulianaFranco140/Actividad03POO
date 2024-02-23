import math

class Circulo:
    def __init__(self,
                 radio,
                 centro):
        self.radio = radio
        self.centro = centro

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia_centro_punto <= self.radio
radio = 5
centro = (0, 0)
circulo = Circulo(radio, centro)
print("Área:", circulo.calcular_area())
print("Perímetro:", circulo.calcular_perimetro())
print("¿El punto (3, 4) pertenece al círculo?", circulo.punto_pertenece((3, 4)))
print("¿El punto (6, 6) pertenece al círculo?", circulo.punto_pertenece((6, 6)))
