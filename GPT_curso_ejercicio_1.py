



class Celular: #------------------------<<<<  esto es la clase 
    def __init__(self, marca, modelo, precio):  # esto es el METODO contructor , le da valores INICIALES al objeto
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

#---------------------------------------------------estos 2 METODOS COMUNES ____  ejecutan una accion espesifica
    def mostrar_info(self):  # INICIO DE METODO 1
        print(f"Celular: {self.marca} {self.modelo}, Precio: ${self.precio}")
    
    def rebajar_precio(self, cantidad):  # INICIO DE METODO 2
            if cantidad <= self.precio:
                self.precio -= cantidad  #----->>>>  -=  significa  restar y guardad
                print(f"Nuevo precio después de rebaja: ${self.precio}")
            else:
                print("❌ No se puede rebajar más de lo que cuesta el celular.")


mi_cel = Celular("Xiaomi", "Redmi Note 12", 5500)  #------<<<< creamos el objeto DEL METODO 1
mi_cel.mostrar_info()    #-------------------------------->>>>> llamamos a  objeto DEL METODO 1

cantidad = int(input("Ingresa $ la rebaja:\n"))
mi_cel.rebajar_precio(cantidad)  #-----------------------------<<<<< creamos el objeto del metodo 2
mi_cel.mostrar_info()       #---------------------------->>>>>>  llamamos al objeto del metodo 2