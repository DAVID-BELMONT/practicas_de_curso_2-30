
def paginar_lista(lista, pagina, por_pagina):
    """
    Divide la lista en páginas.
    Ejemplo: si hay 10 usuarios y pides página=2 con por_pagina=3,
    te devuelve los usuarios del 4 al 6.
    """
    inicio = (pagina - 1) * por_pagina
    fin = inicio + por_pagina
    return lista[inicio:fin]