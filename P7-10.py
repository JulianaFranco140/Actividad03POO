class Cuenta_Bancaria:
    def __init__(self,
                 Numero_Cuenta,
                 Propietarios,
                 Balance) -> None:
        self.numero_cuenta = Numero_Cuenta
        self.propietarios = Propietarios
        self.balance = Balance
    
    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance = self.balance - cuota_manejo
        print ("Sus fondos bancarios son: ", self.balance, " ya aplicada la cuota de manejo.")
    
        
    def depositar (self):
        Decision_Depositar = input("¿Desea depositar más fondos a la cuenta? Si/ No: ")
        if (Decision_Depositar == "Si") or (Decision_Depositar == "si"):
            Monto_Depositar = float(input("Ingrese la cantidad que desea depositar: "))
            self.balance = self.balance + Monto_Depositar
            print ("Los fondos de la cuenta son ", self.balance)
            
        else:
            print ("No hay cambios realizados en el balance de la cuenta.")
            
            
    def retirar (self):
        Decision_Retirar = input("¿Desea retirar fondos de la cuenta? Si/No: ")
        if (Decision_Retirar == "Si") or (Decision_Retirar == "si"):
            Monto_Retirar = float(input("Ingrese la cantidad a retirar: "))
            if (Monto_Retirar > self.balance):
                print ("No hay suficientes fondos en la cuenta.")
            
            else:
                self.balance = self.balance - Monto_Retirar
                print ("Ha retirado ", Monto_Retirar, " de la cuenta, los fondos de su cuenta bancaria son ", self.balance)
        
        else:
            print ("No hay cambios realizados en el balance de la cuenta.")
        
           
        
cuenta = Cuenta_Bancaria("1234567890", ["Juan", "María"], 1000.000)
print("Número de cuenta:", cuenta.numero_cuenta)
print("Propietarios:", cuenta.propietarios)
print("Balance:", cuenta.balance)
cuenta.aplicar_cuota_manejo()
cuenta.depositar()
cuenta.retirar()

