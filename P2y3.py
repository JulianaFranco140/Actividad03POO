class Punto:
    def __init__(self,
                 parametro_x,
                 parametro_y) -> None:
        self.x = parametro_x
        self.y = parametro_y
        
    def Coordenadas(self):
        print ("Las coordenadas son: (",self.x,",", self.y,")") 
        
    def cambiar (self):
        Cambio = input("¿Quiere cambiar las coordenadas del punto? Si/No. ")
        
        if (Cambio == "Si") or (Cambio == "si"):
            self.x = float(input("Ingrese la coordenada del punto en x: "))
            self.y = float(input("Ingrese la coordenada del punto en y: "))
            
            print("Las coordenadas cambiaron a (",self.x,",",self.y,")")
            
        else:
            print ("Las coordenadas no presentan cambios.")
            
    def Calcular_distancia (self):
        print ("Las coordenadas actuales son: (",self.x,",", self.y,")") 
        x1 = self.x
        y1 = self.y
        self.x = float(input("Ingrese la coordenada del punto en x: "))
        self.y = float(input("Ingrese la coordenada del punto en y: "))
        x2 = self.x
        y2 = self.y
        
        distancia = ((x2-x1)** 2 +(y2-y1)**2 )**0.5
        
        print("La distancia entre el punto (",x1,",",y1,") y el punto (",x2,",",y2, ") es ", distancia)
            
            
            
                      
            
Punto1 = Punto(5.0,6.0)
Punto1.Coordenadas()
Punto1.cambiar()
Punto1.Calcular_distancia()
            