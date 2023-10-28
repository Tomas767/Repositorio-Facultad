
# 1.1-----------------------------------------------------------------------------------
def imprimir_menu_desafio_5():
    """Imprime la serie de opciones que ofrece
    la aplicacion Stark5

    return: None
    """

    print("""
---------------------------------------------------------------------------------
                            MENU DE OPCIONES
---------------------------------------------------------------------------------

A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.

---------------------------------------------------------------------------------
""")

# 1.2------------------------------------------------------------------------------------
def stark_menu_principal_defio_5():
    """retorna el valor de la opcion seleccionada

    Returns:
        op(str): opcion validad
    """
    import re

    imprimir_menu_desafio_5()

    op = input("OPCION SELECCIONADA:")

    validacion = re.findall("^[A-N?a-n?]$", op)

    if validacion != []:
        for valor in validacion:
            op = valor.upper()

        return op

    else:
        return "-1"

# 1.3-------------------------------------------------------------------------------------

def stark_marverl_app_5(lista_heroes: list):
    """valida que la opcion seleccionada
    sea correcta

    Args:
        lista_heroes (list): _description_
    """
    import os

    import re

    respuesta = stark_menu_principal_defio_5()

    match(respuesta):
        case "A":
            pass
        case "B":
            pass
        case "C":
            pass
        case "D":
            pass
        case "E":
            pass
        case "F":
            pass
        case "G":
            pass
        case "H":
            pass
        case "I":
            pass
        case "J":
            pass
        case "K":
            pass
        case "L":
            pass
        case "M":
            pass
        case "N":
            pass


# 1.4---------------------------------------------------------------------------------------------

def leer_archivo():
    """lee y retorna el archivo
    como la lista de diccionarios de heroes

    Returns:
        lista_heroes(list): lista de diccionarios
    """
    import json

    with open("data.json" , "r") as archivo:
        datos = json.load(archivo)

    for lista, diccionario in datos.items():
        lista_heroes = diccionario

    return lista_heroes

# 1.5---------------------------------------------------------------------------------------------

# def guardar_archivo(nombre_archivo: str, archivo: str):
    
#     with open(archivo, "w+") as datos:


# 1.6-----------------------------------------------------------------------------------------------

def capitalizar_palabras(string: str):
    """recibe un string como parametro para
    convertir su primer valor en mayuscula

    Args:
        string (str): string a capitalizar

    Returns:
        palabra_capitalizada (str): string ya capitalizado
    """
    import re

    palabras = re.findall("[a-z]+", string)

    if palabras != []:
        for palabra in palabras:
            palabra_capitalizada = " ".join(palabra.capitalize())

    return palabra_capitalizada

# 1.7-----------------------------------------------------------------------------------------------

def obtener_nombre_capitalizado(heroe: dict):
    """recibe un diccionario donde retorna el valor
    almacenado en la clave nombre

    Args:
        heroe (dict): heroe donde se capitalizara la
        su nombre

    Returns:
        heroe (dict): diccionario con su valor
        ya capitalizado
    """
    clave = "nombre"

    for dato in heroe:
        if dato == clave:
            dato = capitalizar_palabras(heroe[clave])

    return heroe

# 1.8-----------------------------------------------------------------------------------------------

def obtener_nombre_y_dato(heroe: dict, elemento: str):
    """recibe el diccionario donde se almacenan los datos
    y segun el elemento que tenga el mismo valor recibido
    se retorna el dato determinado

    Args:
        heroe (dict): diccionario donde se alamacenan los datos
        elemento (str): donde se almacena y destaca el dato
        que buscamos
        dato (str): dato a resaltar

    Returns:
        
    """

    if heroe != {}:
        for clave, valor in heroe.items():
            if elemento == valor:
                dato_deseado = heroe[elemento]

                nombre = obtener_nombre_capitalizado(heroe)

                return dato_deseado, nombre

# 2.1-----------------------------------------------------------------------------------------------

def es_genero(heroe: dict, genero: str):

    clave = "genero"

    if heroe[clave] == genero:
        bandera = True
    
    else:
        bandera = False

    return bandera




