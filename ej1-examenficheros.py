def Leer_Document(fichero):
    """ Funcion para leer la informacion de un fichero y la guarda en
    una variable del tipo lista.
    
    Parámetros:
        -Ruta acceso al fichero: Fichero ya exitente en el cual accedemos a su informacion.
    Salida:
        Una lista con los datos del fichero.
        """
    with open("LibroCuentas.txt", "r") as file:
        x = file.readlines()
        return(x)

"""print(Leer_Document("LibroCuentas.txt"))"""
def Identificar_Pagado(Datos_fichero):
    """ Funcion para identificar PAGADO en una lista.
    
    Parámetros:
        -Lista: Lista que contendra información de la cual sacaremos la informacion.
    Salida:
        Crea un fichero con todas las lineas del documento en las que pone PAGADO.
        """
    with open("PAGADO.txt", "w") as file:
        for lineas in Leer_Document("LibroCuentas.txt"):
            if "PAGADO" in lineas:
                x = lineas
                file.write(x)

Identificar_Pagado(Leer_Document("LibroCuentas.txt"))