from interface.icatalago import ICatalog
from utilidades.enumpaginado import EnumPaginator

class Usuarios(ICatalog):
    def __init__(self):
        self.roles = [ ]

    def paginator(self, page: int, rows: int) -> list[str]:
        if page >= EnumPaginator.MINIMO_VALIDO.value:
            inicio = (page - 1) * rows
            fin = inicio + rows
            return self.roles[inicio:fin]
        return []

    def counter(self) -> int:
        return len(self.roles)

