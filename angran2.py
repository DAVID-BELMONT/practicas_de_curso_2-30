

class Anagrama:
    def __init__(self, palabra1, palabra2):
        self.palabra1 = palabra1.lower()
        self.palabra2 = palabra2.lower()

    def contar_letras(self, palabra):
        conteo = {}
        for letra in palabra:
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
        return conteo

    def es_anagrama(self):
        return self.contar_letras(self.palabra1) == self.contar_letras(self.palabra2)

a = Anagrama("Amor", "Roma")
print(a.es_anagrama())  # True

b = Anagrama("Rana", "Nara")
print(b.es_anagrama())  # True

c = Anagrama("Perro", "Gato")
print(c.es_anagrama())  # False


