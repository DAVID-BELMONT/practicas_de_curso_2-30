

class Carro:
    def __init__(self, marca, modelo, anio, precio = 250000):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def mostrar_info(self) -> None:
        print( f"datos del carro: MARCA: {self.marca} , MODELO: {self.modelo} ,AÑO: {self.anio} , PRECIO {self.precio} ")

    def rebajar_precio(self, cantidad):
        if  cantidad <= self.precio:
            self.precio -= cantidad

            print(f" El precio con rebaja es de :$ {self.precio}")

        else:
            print("No puedes regalar el carro")

    def cambiar_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo
        print(f"El nuevo modelo es: {self.modelo}")

    def es_clasico(self):

        print(f"¿Es clásico? , {self.anio < 2000}")

            

c1 = Carro("Nissan", "Tsuru", 1995, 80000)
c1.mostrar_info()

cantidad = int(input("Ingresa $ la rebaja:\n"))
c1.rebajar_precio(cantidad) 
c1.mostrar_info()       

nuevo_modelo = str(input("Ingresa el nuevo modelo:\n"))
c1.cambiar_modelo(nuevo_modelo)  
c1.mostrar_info()  
c1.es_clasico()

