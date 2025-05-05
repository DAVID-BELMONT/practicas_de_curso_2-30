

from abc import ABCMeta, abstractmethod

class ICatalog(metaclass=ABCMeta):
    """
    Esta clase define la interfaz ICatalog.
    Obliga a las clases que la implementen a definir los métodos:
    - paginator: para paginar resultados
    - counter: para contar registros
    """

    @abstractmethod
    def paginator(self, page: int, rows: int) -> list[dict]:
        pass

    @abstractmethod
    def counter(self) -> int:
        pass



