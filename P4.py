class Rectangulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der
        
    def calcular_perimetro(self):
        largo = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        ancho = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return 2 * (largo + ancho)

    def calcular_area(self):
        largo = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        ancho = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return largo * ancho

    def es_cuadrado(self):
        largo = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        ancho = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return largo == ancho

esquina_sup_izq = (0, 0)
esquina_inf_der = (3, 3)
rectangulo = Rectangulo(esquina_sup_izq, esquina_inf_der)
print("Perímetro:", rectangulo.calcular_perimetro())
print("Área:", rectangulo.calcular_area())
print("¿Es un cuadrado?", rectangulo.es_cuadrado())