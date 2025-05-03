

class Anima(object):

    def __init__(self, color:str, tamanio:str, carnivoro:str, omnivoro:str):
        self.color = color
        self.tamanio = tamanio
        self.carnivoro = carnivoro
        self.omnivoro = omnivoro
    
    
#------------------------------------    

    @property
    def get_color(self) -> str:
        return self.color.upper
    
    @get_color.setter
    def set_color(self, value:str) -> None:
        self.color = value.lower()
#------------------------------------
    @property
    def get_tamanio(self) -> str:
        return self.tamanio.upper
    
    @get_tamanio.setter
    def set_tamanio(self, value:str) -> None:
        self.tamanio = value.lower()    
#------------------------------------    
    
    @property
    def get_carnivoro(self) -> str:
        return self.carnivoro.upper
    
    @get_carnivoro.setter
    def set_carnivoro(self, value:str) -> None:
        self.carnivoro = value.lower()  
        
#------------------------------------
    @property
    def get_omnivoro(self) -> str:
        return self.omnivoro.upper
    
    @get_omnivoro.setter
    def set_omnivoro(self, value:str) -> None:
        self.omnivoro = value.lower()  


#------------------------------------

class Perro(Anima):
    def __init__(self, color, tamanio, carnivoro, obniboro):
        super().__init__(color, tamanio, carnivoro, obniboro)

class Gato(Anima):
    def __init__(self, color, tamanio, carnivoro, obniboro):
        super().__init__(color, tamanio, carnivoro, obniboro)

class Caballo(Anima):
    def __init__(self, color, tamanio, carnivoro, obniboro):
        super().__init__(color, tamanio, carnivoro, obniboro)
        

perro = Perro("blanco" , "chico", "carnivoro", "n/a")
gato = Gato("negro" , "grande" , "carnivoro" , "n/a")


print(perro.color)
print(gato.tamanio)