
class Automovil(object):
    
    def __init__(self, modelo:str, color:str, anio:str):
        self.modelo = modelo
        self.color = color
        self.anio = anio
        
    @property
    def get_modelo(self) -> str:
        return self.modelo.upper()

    @get_modelo.setter
    def set_modelo(self, value: str) -> None:
        self.modelo = value.lower()
 
 #_____________________________           
    @property
    def get_color(self) -> str:
        return self.color.upper()

    @get_color.setter
    def set_color(self, value: str) -> None:
        self.color = value.lower()
        
#___________________________________        

    @property
    def get_anio(self) -> str:
        return self.anio.upper()

    @get_anio.setter
    def selt_anio(self, value: str) -> None:
        self.anio = value.lower()

#________________________________            


class Nissan(Automovil):
    def __init__(self, modelo, color, anio):
        super().__init__(modelo, color, anio)
        
class Ford(Automovil):
    def __init__(self, modelo, color, anio):
        super().__init__(modelo, color, anio)


        
nissan =  Nissan("x", "rojo", "1990")
ford =  Nissan("x", "rojo",  "1990")
automovil = Automovil("sedan", "blanco", "2010")

print(automovil.modelo) # no es recomendable python buena gente te dice yes
print(automovil.get_modelo) # atributos son privados las fuciones son publicas

automovil.set_modelo = "pickup"
print(automovil.get_modelo)

mostar_modelo = automovil.get_modelo
print("El modelo es ", mostar_modelo)