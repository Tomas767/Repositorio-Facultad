
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

def guardar_archivo(nombre_archivo, archivo):
    if type(nombre_archivo) == str and nombre_archivo != "":
        with open(nombre_archivo, 'w+') as archivo:
            archivo.write(archivo)

        print(f"Se creó el archivo o se escribio en el arhivo: {nombre_archivo}")

        return True

    else:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False


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
        heroe (str): nombre con su valor
        ya capitalizado
    """
    clave = "nombre"

    nombre = capitalizar_palabras(heroe[clave])

    nombre = clave + ": " + nombre

    return nombre

# 1.8-----------------------------------------------------------------------------------------------

def obtener_nombre_y_dato(heroe: dict, dato: str):
    """recibe el diccionario donde se almacenan los datos
    y segun el dato que tenga el mismo valor recibido
    se retorna el dato determinado

    Args:
        heroe (dict): diccionario donde se alamacenan los datos
        dato (str): donde se almacena y destaca el dato
        que buscamos
        dato (str): dato a resaltar

    Returns:
        dato_deseado, nombre(tuple): devuelve el nombre y el dato 
        especificado
        
    """

    dato_deseado = heroe[dato]

    nombre = obtener_nombre_capitalizado(heroe)

    nombre_dato = nombre + "|" + dato + ": " + dato_deseado

    return nombre_dato

# 2.1-----------------------------------------------------------------------------------------------

def es_genero(heroe: dict, genero: str):
    """valida si el heroe es el genero
    especificado

    Args:
        heroe (dict): diccionario del heroe
        a validar su genero
        genero (str): genero a comparar

    Returns:
        bandera (bool): valida si es o no
        el genero que se desea
    """

    clave = "genero"

    if clave in heroe:
        if heroe[clave] == genero:
            bandera = True
        
        else:
            bandera = False
    
        return bandera
    
    else:
        print("ERROR NO EXISTE EL GENERO DEL HEROE")

# 2.2-----------------------------------------------------------------------------------------------

def stark_guardar_heroe_genero(heroes: list, genero: str):
    """almaceno todos lo heroes que coincidan
    con el genero establecido

    Args:
        heroes (list): lista de heroes y sus datos
        genero (str): genero establecido

    Returns:
        bandera (bool): validacion de que se almaceno el archivo
    """

    for heroe in heroes:
        validacion = es_genero(heroe, genero)

        if validacion:
            nombre_heroe = obtener_nombre_capitalizado(heroe)

            match(genero):
                case "F":
                    bandera = guardar_archivo("heroes_F.csv", nombre_heroe + " ,")

                case "M":
                    bandera = guardar_archivo("heroes_M.csv", nombre_heroe + " ,")

                case "NB":
                    bandera = guardar_archivo("heroes_NB.csv", nombre_heroe + " ,")


    return bandera

# 3.1-----------------------------------------------------------------------------------------------

def calcular_min_genero(heroes: list, dato: str, genero: str):
    """calcula el valor minimo del dato pasado
    y segun el genero establecido devuelve el heroe
    con el valor minimo del dato encontrado

    Args:
        heroes (list): lista de heroes y sus datos
        dato (str): dato establecido con medida
        numerica
        genero (str): genero establecido 

    Returns:
        heroe_min(dict): heroe con el valor del dato
        mas bajo
    """
    bandera = True

    for heroe in heroes:
        for dato in heroe:
            if heroe(dato) == genero:
                if bandera:
                    heroe_min = heroe

                    bandera = False

                elif heroe(dato) < heroe_min(dato):
                    heroe_min = heroe
    
    return heroe_min

# 3.2-----------------------------------------------------------------------------------------------

def calcular_max_genero(heroes: list, dato: str, genero: str):
    """calcula el valor maximo del dato pasado
    y segun el genero establecido devuelve el heroe
    con el valor maximo del dato encontrado

    Args:
        heroes (list): lista de heroes y sus datos
        dato (str): dato establecido con medida
        numerica
        genero (str): genero establecido 

    Returns:
        heroe_min(dict): heroe con el valor del dato
        mas alto
    """
    bandera = True

    for heroe in heroes:
        for dato in heroe:
            if heroe(dato) == genero:
                if bandera:
                    heroe_max = heroe

                    bandera = False

                elif heroe(dato) > heroe_max(dato):
                    heroe_max = heroe

    return heroe_max

# 3.3-----------------------------------------------------------------------------------------------

def calcular_max_min_dato_genero(heroes: list, genero: str, dato: str, analisis: str):
    """analisa el minimo o maximo segun lo que se pida
    y retorna el diccionario del heroe segun su genero

    Args:
        heroes (list): lista de diccionarios con los datos
        de los heroes
        genero (str): genero especifico F/M/NB 
        dato (str): dato a buscar en los heroes
        analisis (str): si se desea el maximo o minimo
        del heroe

    Returns:
        heroe(dict): heroe con el maximo o minimo de los datos
        segun su genero
    """
    match(analisis):
        case "minimo":
            heroe = calcular_min_genero(heroes, dato, genero)
        case "maximo":
            heroe = calcular_max_genero(heroes, dato, genero)

    return heroe

# 3.4-----------------------------------------------------------------------------------------------

def stark_calcular_imprimir_guarda_heroe_genero(heroes: list, analisis: str, 
dato:str, genero:str):
    """calcula el minimo o maximo de un dato segun el
    genero establecido

    Args:
        heroes (list): lista de diccionarios con
        los datos de los heroes
        analisis (str): maximo o minimo
        dato (str): dato existente en el heroe
        genero (str): genero del heroe

    Returns:
        validacion (bool): validacion de que se realizo el 
        guardado del archivo
    """

    heroe = calcular_max_min_dato_genero(heroes, genero, dato, analisis)

    nombre_dato = obtener_nombre_y_dato(heroe, dato)

    analisis_completo = analisis + dato + ":" + nombre_dato

    print (analisis_completo)

    nombre_archivo = "heroes_" + analisis + "_" + dato + "_" + genero + ".csv"

    validacion = guardar_archivo(nombre_archivo, analisis_completo)

    return validacion

# 4.1-----------------------------------------------------------------------------------------------

def sumar_dato_heroe_genero(heroes: list, clave: str, genero: str, valor_genero: str)-> (int or float):
    """recorre la lista recibida y analiza para acomular los valores almacenados en los
    diccionarios generales o especificos en caso de condicion extra

    Args:
        heroes (list): lista donde se almacenan los diccionarios que se iteraran
        clave (str): clave de diccionario donde se almacenan los valores
        que se desean sumar 
        genero (str):clave que agrupa 
        determinados valores especificos
        valor_genero (str): valor especifico que agrupa ciertos
        elementos mediante condicional

    Returns:
        int or float: la suma total valores acomulados dentro de la lista
    """
    suma = 0

    for heroe in heroes:
        if heroe != {} and heroe[genero] == valor_genero:
            for elemento in heroe:
                if elemento == clave and (type(heroe[elemento]) ==  float or type(heroe[elemento]) == int):
                    suma += heroe[elemento]

    if suma == 0:
        suma = -1
    
    return suma

# 4.2-----------------------------------------------------------------------------------------------

def cantidad_heroes_genero(heroes: list, genero: str):
    suma_heroes = 0

    for heroe in heroes:
        if heroe["genero"] == genero:
            suma_heroes += 1
    
    return suma_heroes

# 4.3-----------------------------------------------------------------------------------------------

def dividir(divisor: int or float, dividendo: int or float)-> (float or int) and bool:
    """divide dos numeros recibidos unicamenten caso
    de que los numeros sean enteros o flotantes y que 
    el divisor recivido no sea 0
    

    Returns:
        (float or int) and bool: el resultado de la division y el booleando
        que determina si se realizo la dvision o no
    """
    resultado = None

    bandera_5 = False

    if divisor != 0:
        resultado = dividendo / divisor

        bandera_5 = True
    
    else:
        print("No se puede realizar la division/ el divisor es 0")

    return resultado, bandera_5



def sacar_promedio(heroes: list, clave:str, genero: str, valor_genero: str) -> (int or float):
    """a traves de la lista recibida y la clave donde se almacena los valores que se desean
    calcular su promedio suma los valores y la cantidad de diccionarios que poseen
    el mismo para asi sacar el promedio

    Args:
        heroes (list): lista donde se almacenan los diccionarios que se iteraran
        clave (str): clave de diccionario donde se almacenan los valores
        que se desean sumar 
        genero (str):clave que agrupa 
        determinados valores especificos
        valor_genero (str): valor especifico que agrupa ciertos
        elementos mediante condiciona

    Returns:
        int or float: devuleve el promedio total de los valores encontrados 
        segun cuantos diccionarios lo poseean
    """
    contador = 0

    promedio = 0

    suma_datos = sumar_dato_heroe_genero(heroes, clave, genero, valor_genero)

    heroes_genero = cantidad_heroes_genero(heroes, genero)

    promedio, bandera_5= dividir(heroes_genero, suma_datos)

    return promedio, bandera_5

# 4.4-----------------------------------------------------------------------------------------------

def stark_calcular_imprimir_guardar_promedio_altura_genero(heroes: list,valor_genero: str ,clave = "altura", clave_genero = "genero"):
    if heroes != []:
        match(valor_genero):
            case "M":
                promedio, bandera = sacar_promedio(heroes, clave, clave_genero, valor_genero)

                if bandera:
                    resolucion = clave + " promedio " + "genero " + valor_genero + ": " + promedio

                    nombre_archivo = "heroes_promedio_" + clave + "_" + valor_genero + ".csv"

                    bandera1 = guardar_archivo(nombre_archivo, resolucion)

                    return promedio, bandera1

                else:
                    print("no se pudo realizar el promedio")

            case "F":
                promedio, bandera = sacar_promedio(heroes, clave, clave_genero, valor_genero)
                
                if bandera:
                    resolucion = clave + " promedio " + "genero " + valor_genero + ": " + promedio

                    nombre_archivo = "heroes_promedio_" + clave + "_" + valor_genero + ".csv"

                    bandera1 = guardar_archivo(nombre_archivo, resolucion)

                    print(resolucion)

                    return promedio, bandera1

                else:
                    print("no se pudo realizar el promedio")

            case other:
                print("genero no admitido")

    else:
        print("ERROR: Lista de heroes vacía")

# 5.1-----------------------------------------------------------------------------------------------
def contavilizar(datos: list ,cualidad: str, clave: str):
    count = 0

    for dato in datos:
        # print(dato[clave] + "-----" + cualidad)
        if cualidad == dato[clave]:
            count += 1
    
    return count

def crear_set(datos: list, cualidad: str):
    set_cualidades = []

    for dato in datos:
        for clave, valor in dato.items():
            if clave == cualidad and valor not in set_cualidades:
                set_cualidades.append(valor)

    return set_cualidades

def calcular_cantidad_tipo(heroes, clave_valores):
    """recorre los datos de los heroes sumando cuantos tienen
    cada tipo de cualidad y retorna las cualidades y el total
    de heroes que las poseen

    Args:
        heroes (list): lista con los datos de los heroes
        clave_valores (str): clave donde se almacenan
        los valores o cualidades que se buscan

    Returns:
        diccionario_valores(dict): las cualidades y cuantos heroes
        tienen cada una de ellas como valor numerico
    """
    if heroes != []:
        diccionario_valores = {}

        for heroe in heroes:
            valor = capitalizar_palabras(heroe[clave_valores])
            
            heroe[clave_valores] = valor

        set_valores = crear_set(heroes, clave_valores)

        for valor in set_valores:
            contador = contavilizar(heroes, valor, clave_valores)

            diccionario_valores[valor] = contador

        return diccionario_valores

    else:
        dict_error = {}

        dict_error["Error"] = "la lista esta vacia"

# 5.2-----------------------------------------------------------------------------------------------
def guardar_cantidad_heroes_tipo(diccionario_valores: dict, clave_valor: str):

    for valor in diccionario_valores:
        resolucion = ("Caracteristicas " + clave_valor + " " + valor
+ " - " + "Cantidad de heroes: " + diccionario_valores[valor])

        nombre_archivo = "heroes_cantidad_" + clave_valor + ".csv"

        bandera = guardar_archivo(nombre_archivo, resolucion)

        if not bandera:
            print("hubo un error")

            return bandera
        
    return bandera

# 5.3-----------------------------------------------------------------------------------------------

def stark_calcular_cantidad_por_tipo(heroes: list, clave_valor: str):
    if heroes != []:
        diccionario_valores = calcular_cantidad_tipo(heroes, clave_valor)

        bandera = guardar_cantidad_heroes_tipo(diccionario_valores, clave_valor)

    return bandera