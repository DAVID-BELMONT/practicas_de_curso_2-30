



from interface.icatalago import ICatalog

class Roles(ICatalog):

    def __init__(self):
        
        self.lista_roles = []

    def paginator(self, page: int, rows: int) -> list[str]:
       
        inicio = (page - 1) * rows
        fin = inicio + rows
        return self.lista_roles[inicio:fin]

    def counter(self) -> int:
        return len(self.lista_roles)
