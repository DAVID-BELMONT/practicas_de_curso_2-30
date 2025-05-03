

class Listas(object):
    def __init__(self):
        pass
    def lista_simple()-> list:
       # lista = []
        lista_dos:list[str] = list()     # esta forma de lista es la mehjor para fortalecer el tipado 
        lista_dos = list()
        lista_con_datos:list[int] = [1, 2, 3, 4, 5, 6,]
        lista_dos.append("david")
        lista_dos.append("juan")
        lista_dos.append("pedro")
        return[lista_dos, lista_con_datos]
    
    def agregar_idex(self, list:list[str], index:int, value:str)-> None:
        list.insert(index, value)

    def eliminar_dato(self, lista:list[str], value:str) -> None:
        lista.remove(value)

    def juntar_lista(self, lista:list[str] lista_dos:list[int]) -> list:
    lista_junta = lista + lista_dos





