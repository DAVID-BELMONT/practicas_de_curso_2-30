

class Numeros:
    def __init__(self, num1:int, num2:int):
        self._numero1 = num1
        self._numero2 = num2

#--------------------------------------------------------- numero 1

    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self, value):
        self._numero1 = value
#--------------------------------------------------------- numero 2
    @property
    def numero2(self):
        return self._numero2
    
    
    @numero2.setter
    def numero2(self, value):
        self._numero2 = value
       
#--------------------------------------------------------- operaciones hija

 
class Operacione(Numeros):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def suma(self):
        resultado_suam = self.numero1 + self.numero2 # CREAMOS RESULTADO_SUMA
        print(f"La suma es: {resultado_suam}") 

    def resta(self):
        resultado_resta = self.numero1 - self.numero2 # CREAMOS RESULTADO_RESTA 
        print(f"La resta es: {resultado_resta}")         

    def division(self):
        if self.numero2 == 0: # esto es para que no salga error en la dividion
            print("no se poede dividir ")

        else:
            resultado_divicion = self.numero1 / self.numero2 # CREAMOS RESULTADO_DIVICION
            print(f"La divicion es: {resultado_divicion}")         
        
    def multiplicacion(self):
        resultado_multiplicacion = self.numero1 * self.numero2 # CREAMOS RESULTADO_MULTIPLICACION
        print(f"La multiplicacion es: {resultado_multiplicacion}") 

num1 = int(input("Ingresa el primer número:\n"))
num2 = int(input("Ingresa el segundo número:\n"))

op = Operacione(num1, num2)   # SI NO CREAMOS EL OBJETO  _____ NUNCA VA ADAR UNA OPERACION
op.suma()
op.resta()
op.division()
op.multiplicacion()