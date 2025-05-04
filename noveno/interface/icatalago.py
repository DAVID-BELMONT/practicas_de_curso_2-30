

from abc import ABC, ABCMeta, abstractmethod

class ICatalog(metaclass=ABCMeta):

    @abstractmethod
    def paginator(self, page: int, rows: int) -> list[str]:
        pass

    @abstractmethod
    def counter(self) -> int:
        pass
