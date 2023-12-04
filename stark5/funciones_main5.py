def armar_validaciones(lista_nombres_banderas: list, lista_banderas: list):
    diccionario_validaciones = {}

    for i in range(len(lista_nombres_banderas)):
        diccionario_validaciones[lista_nombres_banderas[i]] = lista_banderas[i]
    
    return diccionario_validaciones

def recorrer_archivos(diccionario_validaciones: dict):
    import csv

    for validacion in diccionario_validaciones:
        match(validacion):
            case "bandera_C":
                if diccionario_validaciones[validacion]:
                    with open("heroes_maximo_altura_M.csv", "r+") as archivo:
                        lectura = csv.reader(archivo)

                        for fila in lectura:
                            print(fila[0])
                
                else:
                    print("no se genero el arhivo")

            case "bandera_D":
                if diccionario_validaciones[validacion]:
                    with open("heroes_maximo_altura_F.csv", "r+") as archivo:
                        lectura = csv.reader(archivo)

                        for fila in lectura:
                            print(fila[0])

                else:
                    print("no se genero el arhivo")

            case "bandera_E":
                if diccionario_validaciones[validacion]:
                    with open("heroes_minimo_altura_M.csv", "r+") as archivo:
                        lectura = csv.reader(archivo)

                        for fila in lectura:
                            print(fila[0])

                else:
                    print("no se genero el arhivo")

            case "bandera_F":
                if diccionario_validaciones[validacion]:
                    with open("heroes_minimo_altura_F.csv", "r+") as archivo:
                        lectura = csv.reader(archivo)

                        for fila in lectura:
                            print(fila[0])

                else:
                    print("no se genero el arhivo")

            
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

    bandera_C = False

    bandera_D = False

    bandera_E = False

    bandera_F = False

    bandera_J = False

    bandera_K = False

    bandera_L = False

    try:
        with open("heroes_segun_color_ojos.csv", "r") as file:
            bandera_M = True
    
    except FileNotFoundError:
        bandera_M = False

    try:
        with open("heroes_segun_color_pelo.csv", "r") as file:
            bandera_N = True
    
    except FileNotFoundError:
        bandera_N = False

    while True:
        respuesta = stark_menu_principal_defio_5()

        match(respuesta):
            case "A":
                print("""Los heroes del genero masculino son:
-----------------------------------""")
                for heroe in lista_heroes:
                    validacion = es_genero(heroe, "M")

                    if validacion:
                        dato = obtener_nombre_capitalizado(heroe)

                        print(dato)
            case "B":
                print("""Los heroes del genero femenino son:
-----------------------------------""")
                for heroe in lista_heroes:
                    validacion = es_genero(heroe, "F")

                    if validacion:
                        dato = obtener_nombre_capitalizado(heroe)

                        print(dato)

            case "C":
                bandera_C = stark_calcular_imprimir_guarda_heroe_genero(lista_heroes, "maximo", "altura", "M")

            case "D":
                bandera_D = stark_calcular_imprimir_guarda_heroe_genero(lista_heroes, "maximo", "altura", "F")

            case "E":
                bandera_E = stark_calcular_imprimir_guarda_heroe_genero(lista_heroes, "minimo", "altura", "M")

            case "F":
                bandera_F = stark_calcular_imprimir_guarda_heroe_genero(lista_heroes, "minimo", "altura", "F")

            case "G":
                resultado, bandera = stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, "M")

                print(resultado)

            case "H":
                resultado, bandera = stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, "F", "altura", "genero")

                print(resultado)

            case "I":
                diccionario_validaciones = armar_validaciones(["bandera_C", "bandera_D", "bandera_E", "bandera_F"], [bandera_C, bandera_D, bandera_E, bandera_F])

                recorrer_archivos(diccionario_validaciones)

            case "J":
                if not bandera_J:
                    bandera_J = stark_calcular_cantidad_por_tipo(lista_heroes, "color_ojos")

            case "K":
                if not bandera_K:
                    bandera_K = stark_calcular_cantidad_por_tipo(lista_heroes, "color_pelo")

            case "L":
                if not bandera_L:
                    bandera_L = stark_calcular_cantidad_por_tipo(lista_heroes, "inteligencia")

            case "M":
                if not bandera_M:
                    set_elementos = obtener_lista_de_tipos(lista_heroes, "color_ojos")

                    diccionario_heroes = obtener_heroes_por_tipo(lista_heroes, set_elementos, "color_ojos")

                    bandera_M = guardar_heroe_por_tipo(diccionario_heroes, "color_ojos")
                else:
                    print("ya se creo el archivo")

            case "N":
                if not bandera_N:
                    set_elementos = obtener_lista_de_tipos(lista_heroes, "color_pelo")

                    diccionario_heroes = obtener_heroes_por_tipo(lista_heroes, set_elementos, "color_pelo")

                    bandera_N = guardar_heroe_por_tipo(diccionario_heroes, "color_pelo")
                else:
                    print("ya se creo el archivo")

        os.system("pause")

        os.system("cls")


# 1.4---------------------------------------------------------------------------------------------

def leer_archivo():
    """lee y retorna el archivo
    como la lista de diccionarios de heroes

    Returns:
        lista_heroes(list): lista de diccionarios
    """
    import json

    with open("STARK_INT\stark5\heroes.json", "r") as archivo:
        datos = json.load(archivo)

    for lista, diccionario in datos.items():
        lista_heroes = diccionario

    return lista_heroes

# 1.5---------------------------------------------------------------------------------------------

def guardar_archivo(nombre_archivo, archivo, archivo_largo_corto):
    import csv
    match(archivo_largo_corto):
        case "corto":
            if type(nombre_archivo) == str and nombre_archivo != "":

                with open(nombre_archivo, 'a') as file:
                    file.write(archivo + "\n")

                print(f"Se creó el archivo o se escribio en el arhivo: {nombre_archivo}")

                return True

            else:
                print(f"Error al crear el archivo: {nombre_archivo}")

                return False
        case "largo":
            if type(nombre_archivo) == str and nombre_archivo != "":

                with open(nombre_archivo, 'a') as file:
                    for x in archivo:
                        file.write(f"{x}\n")

                print(f"Se creó el archivo o se escribio en el arhivo: {nombre_archivo}")

                return True

            else:
                print(f"Error al crear el archivo: {nombre_archivo}")

                return False

def guardar_archivo_max_min(nombre_archivo, archivo):
    if type(nombre_archivo) == str and nombre_archivo != "":

        with open(nombre_archivo, 'w+') as file:
            file.write(archivo)

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

    string = string.lower()

    palabras = re.findall("[a-z]+-?[a-z]+|[a-z]+\s[a-z]+", string)

    if palabras != []:
        if type(palabras) == list:
            for i in range(len(palabras)):
                palabras[i] = palabras[i].capitalize()

            palabra_capitalizada = " ".join(palabras)
    
    else:
        palabra_capitalizada = "N/A"


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
                    bandera = guardar_archivo("heroes_F.csv", nombre_heroe + " ,", "corto")

                case "M":
                    bandera = guardar_archivo("heroes_M.csv", nombre_heroe + " ,", "corto")

                case "NB":
                    bandera = guardar_archivo("heroes_NB.csv", nombre_heroe + " ,", "corto")


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
        if heroe["genero"]== genero:
            if bandera:
                heroe_min = heroe

                bandera = False

            elif float(heroe[dato]) < float(heroe_min[dato]):
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
        if heroe["genero"] == genero:
            if bandera:
                heroe_max = heroe

                bandera = False

            elif float(heroe[dato]) > float(heroe_max[dato]):
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
    print(nombre_dato)
    analisis_completo = analisis +" "+ dato + ": " + nombre_dato

    nombre_archivo = "heroes_" + analisis + "_" + dato + "_" + genero + ".csv"

    validacion = guardar_archivo_max_min(nombre_archivo, analisis_completo)

    return validacion

# 4.1-----------------------------------------------------------------------------------------------

def sumar_dato_heroe_genero(heroes: list, clave: str, clave_genero: str, valor_genero: str)-> (int or float):
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
        if heroe != {} and heroe[clave_genero] == valor_genero:
            suma += float(heroe[clave])

    return suma

# 4.2-----------------------------------------------------------------------------------------------

def cantidad_heroes_genero(heroes: list, genero: str):
    suma_heroes = 0

    for heroe in heroes:
        if heroe["genero"] == genero:
            suma_heroes += 1

    return suma_heroes

# 4.3-----------------------------------------------------------------------------------------------

def dividir(divisor: int, dividendo: (float or int)):
    """genera una division y retorna el resultado

    Args:
        divisor (int): numero que divide
        dividendo (float or int): numero a dividir

    Returns:
        resutlado, bandera_5 (any, bool): _description_
    """
    resultado = None

    bandera_5 = False

    if divisor != 0:
        resultado = dividendo / divisor

        bandera_5 = True
    
    else:
        resultado = -1

        print("No se puede realizar la division/ el divisor es 0")

    return resultado, bandera_5



def sacar_promedio(heroes: list, clave:str, clave_genero: str, valor_genero: str) -> (int or float):
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

    suma_datos = sumar_dato_heroe_genero(heroes, clave, clave_genero, valor_genero)

    heroes_genero = cantidad_heroes_genero(heroes, valor_genero)

    promedio, bandera_5= dividir(heroes_genero, suma_datos)

    return promedio, bandera_5

# 4.4-----------------------------------------------------------------------------------------------

def stark_calcular_imprimir_guardar_promedio_altura_genero(heroes: list,valor_genero: str ,clave = "altura", clave_genero = "genero"):
    if heroes != []:
        match(valor_genero):
            case "M":
                promedio, bandera = sacar_promedio(heroes, clave, clave_genero, valor_genero)

                if bandera:
                    resolucion = clave + " promedio " + "genero " + valor_genero + ": " + str(promedio)

                    nombre_archivo = "heroes_promedio_" + clave + "_" + valor_genero + ".csv"

                    bandera1 = guardar_archivo_max_min(nombre_archivo, resolucion)

                    return resolucion, bandera1

                else:
                    print("no se pudo realizar el promedio")

            case "F":
                promedio, bandera = sacar_promedio(heroes, clave, clave_genero, valor_genero)
                
                if bandera:
                    resolucion = clave + " promedio " + "genero " + valor_genero + ": " + str(promedio)

                    nombre_archivo = "heroes_promedio_" + clave + "_" + valor_genero + ".csv"

                    bandera1 = guardar_archivo_max_min(nombre_archivo, resolucion)

                    return resolucion, bandera1

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
        print(cualidad, "------------", dato[clave])
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
        print(set_valores)
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
+ " - " + "Cantidad de heroes: " + str(diccionario_valores[valor]))

        nombre_archivo = "heroes_cantidad_" + clave_valor + ".csv"

        bandera = guardar_archivo(nombre_archivo, resolucion, "corto")

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

# 6.1-----------------------------------------------------------------------------------------------

def obtener_lista_de_tipos(heroes: list, clave_valores: str):
    lista_valores = []

    for heroe in heroes:
        valor = heroe[clave_valores]

        if valor == "":
            valor = "N/A"
            
            lista_valores.append(valor)
        
        else:
            valor = capitalizar_palabras(valor)

            lista_valores.append(valor)
    
    lista_valores = set(lista_valores)

    return lista_valores

# 6.2-----------------------------------------------------------------------------------------------

def normalizar_dato(valor: any, valor_por_defecto: str):
    import re

    retorno = re.findall("^[\s]", valor)

    if retorno == [] and valor != "":
        return valor

    else:
        return valor_por_defecto

# 6.3-----------------------------------------------------------------------------------------------

def normalizar_heroe(heroe: dict, clave_valor: str):
    """normaliza el nombre y el dato sobre el cual
    se desea trabajar a traves de su key en el 
    diccionario

    Args:
        heroe (dict): datos del heroe
        clave_valor (str): clave

    Returns:
        heroe (dict): heroe con los datos ya normalizados
    """
    heroe["nombre"] = capitalizar_palabras(heroe["nombre"])

    valor = normalizar_dato(heroe[clave_valor], "N/A")

    if valor != "N/A":
        heroe[clave_valor] = capitalizar_palabras(valor)
        
    else:
        heroe[clave_valor] = "N/A"

    return heroe

# 6.4-----------------------------------------------------------------------------------------------

def obtener_heroes_por_tipo(heroes: list, set_valores: set, clave_valores: str):
    tipos = {}

    for valor in set_valores:
        if valor not in tipos:
            tipos[valor] = []

        for heroe in heroes:
            heroe = normalizar_heroe(heroe, clave_valores)
            if valor == heroe[clave_valores]:
                tipos[valor].append(heroe["nombre"])
    
    return tipos

# 6.5-----------------------------------------------------------------------------------------------

def guardar_heroe_por_tipo(diccionario_tipos: dict, clave_valores: str):
    lista_tipos = []

    for tipos in diccionario_tipos:
        heroes = " | ".join(diccionario_tipos[tipos])

        texto = clave_valores + " " + tipos + ": " + heroes

        archivo = "heroes_segun_" + clave_valores + ".csv"

        lista_tipos.append(texto)

    bandera = guardar_archivo(archivo, lista_tipos, "largo")

    return bandera
