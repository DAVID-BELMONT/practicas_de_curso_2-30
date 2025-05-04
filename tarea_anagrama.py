


class BuscadorAnagramas:
    def __init__(self, ruta_diccionario:str):  # CREAMOS LA INSTANCIA PARA EL DICCIONARIO 
        self.diccionario = self.cargar_diccionario(ruta_diccionario)

    def cargar_diccionario(self, ruta):     # CARGAMOS EL DICCIONARIO
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return [linea.strip().lower() for linea in archivo]

    def es_anagrama(self, palabra1, palabra2):  # sorted() solo reordena los elementos de cualquier cosa que sea una secuencia (lista, cadena, tupla, etc.) y devuelve una nueva lista ordenada.
        return sorted(palabra1) == sorted(palabra2) and palabra1 != palabra2

    def encontrar_anagramas(self, palabra): # compara si las palabras reordenadas tiene una coincidencia en el diccionario
        palabra = palabra.lower()
        return [p for p in self.diccionario if self.es_anagrama(palabra, p)]

    def iniciar_busqueda(self):
        print()
        print()
        print("Escribe palabras para encontrar sus anagramas. Escribe 'salir' para terminar.")
        print()

        while True:
            palabra = input("Ingresa una palabra:  ")

            if palabra.lower() == 'salir':
                print()
                print("¡Nos vemos, PRINCIPE DEL RAP! ") #pudes usar \n para realizar esos saltos de linea en vez de imprimir lineas en blanco.
                print()
                break

            anagramas = self.encontrar_anagramas(palabra)

            if anagramas:
                print()
                print(f"---<<<Anagramas encontrados para >>--'{palabra}'--<<: {', '.join(anagramas)} >>>---")
                print()

            else:
                print()
                print(f" No se encontraron anagramas para '{palabra}'.")
                print()


# --- MAIN ---
if __name__ == '__main__': # __name__ ejecuta la importacion del diccionario TXT de la rura  
    ruta_diccionario = r"\\NAS_MS\david\CURSO PYTHON\diccionario-espanol-txt-master\0_palabras_todas.txt"
    buscador = BuscadorAnagramas(ruta_diccionario)
    buscador.iniciar_busqueda()
