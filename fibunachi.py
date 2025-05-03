
# serie de Fibonacci

a = 0    # siempre comienza con 0 y 1 
b = 1
limite = 1000    #  es necesaria poner un fin al buque

while a <= limite:    # se repite mientras sea menos al limite 1000
    print(a, end= " ")    #imprime el valor de a hacia la derecha 
    c = a + b               # primero se pone la variable y despues se pone la operacion para que se almacene en la variable
    a=b                     # a toma le valor de b
    b=c                     # b toma el valor generado en la suam =c
    
    
    """
    
    a=0 ----imprime --0 --- ES LA PRIMERA CONDICION DEL PROGRAMA
    b=1
    __---_
     
    c=a+b
    c =0+1   --- 1
    
    a=b   
    a=1
    
    b=c
    b=1
    ---------------
    a=1 -----imprime ---1
    b=1
        
    c=a+b
    c = 1+1  --- 2
    
    a=b   
    a=1
    
    b=c
    b=2
-----------------
    a=1 -----imprime ---1
    b=2
        
    c=a+b
    c = 1+2  --- 3
    
    a=b   
    a=2
    
    b=c
    b=3
   -----------------   
    
    a=2---impime ---2
    b=3
    
    
    c=a+b
    c = 2+3  --- 5
    
    a=b   
    a=3
    
    b=c
    b=5
    
   --------------------

    a=3 ----- impime ---3
    b=5
    
    
    c=a+b
    c = 3+5  --- 8
    
    a=b   
    a=5
    
    b=c
    b=8
    
    """
    
    """
         se imprime cero ya que el comenzamos en a=0
    
 Paso	    a	b	c = a + b	Impresión de valor de a
    1   	0	1	1	        0
    2	    1	1	2	        1
    3   	1	2	3	        1
    4   	2	3	5	        2
    5   	3	5	8	        3
    6   	5	8	13	        5
    7   	8	13	21	        8
    8   	13	21	34	        13
    
    """