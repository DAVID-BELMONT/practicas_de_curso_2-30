


class Carro:
    def __init__(self, marca, modelo, anio, precio=250000):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def mostrar_info(self):
        print(f"Carro: {self.marca} {self.modelo} ({self.anio}) - ${self.precio}")

    def es_clasico(self):
        return self.anio < 2000
class CarroElectrico(Carro):
    def __init__(self, marca, modelo, anio, precio, autonomia):
        # Reutiliza el constructor del padre con super()
        super().__init__(marca, modelo, anio, precio)
        self.autonomia = autonomia  # nuevo atributo

    def mostrar_info(self):
        # Sobreescribimos el método para mostrar también autonomía
        print(f"Carro Eléctrico: {self.marca} {self.modelo} ({self.anio}) - ${self.precio}")
        print(f"Autonomía: {self.autonomia} km")

class Camioneta(Carro):
    def __init__(self, marca, modelo, anio, precio, traccion=0):
        # Reutiliza el constructor del padre con super()
        super().__init__(marca, modelo, anio, precio)
        self.traccion = traccion  # nuevo atributo

    def mostrar_info(self):
        # Sobreescribimos el método para mostrar también traccion
        print(f"Camioneta: {self.marca} {self.modelo} ({self.anio}) - ${self.precio}")
        print(f"Es traccion: {self.traccion}")
    

    def es_4x4(self):
        es = self.traccion == "4x4"
        print(f"¿Es 4x4?: {es}")
        

c2 = CarroElectrico("Tesla", "Model 3", 2022, 900000, 450) #las variables tienen que tener sentido en este caso yo hubiera puesto un carro_electronico como variable.
c2.mostrar_info()

if c2.es_clasico():
    print("Este Tesla es un clásico.")
else:
    print("Este Tesla es moderno.")


#---------------  mostra herencia agregando si es 4x4 o no la camineta


c3 = Camioneta("toyota", "hilux", 2020, 50000, "4x4")
c3.mostrar_info()
c3.es_4x4()
