

class Ciclos(object):
    def __init__(self, letras:str, contador:int):
        self.letras = letras
        self.contador = contador
        

    def mientras(self) -> None:
        mensaje = input("quieres hacer una tabla de multiplicar ¿ SI o NO ?").lower()
        while mensaje == "si":
            i = self.contador
            numero = int(input("ingrese un numero"))
            while i <= 10:
                print(f"{i} x {numero} = {numero * i}")
                i += 1
            mensaje = input("quieres hacer una tabla de multiplicar ¿ SI o NO ?").lower()



    class Ciclos(object):
    def __init__(self, letras: str, contador: int):
        self.letras = letras
        self.contador = contador

    def mientras_recursivo(self) -> None:
        mensaje = input("¿Desea hacer una tabla de multiplicar? (si/no): ").lower()
        if mensaje == "si":
            i = self.contador
            numero = int(input("Ingrese un número: "))
            while i <= 10:
                print(f"{i} x {numero} = {numero * i}")
                i += 1
            self.mientras_recursivo()  #  llamada correcta a sí misma

    def para(self)-> None:
        mensaje = input("¿Desea hacer una tabla de multiplicar? (si/no): ").lower()
        while mensaje == "si":
            numero = int(input("ingrese un numero!!"))
            for item in range(1,11):
                print(f"{item} x {numero} = {numero * item}")
            mensaje = input("¿Desea hacer una tabla de multiplicar? (si/no): ").lower()


ciclos = Ciclos("", 1) 
ciclos.mientras()
ciclos.mientras_recursivo()
ciclos.para()