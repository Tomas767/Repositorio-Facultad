# 1.1 --------------------------------------------------------
def extraer_iniciales(dato: dict, clave: str):
    """valida que la clave exista y que su valor
    no contenga un str vacio, devolviendo las 
    inciales de los nombres

    Args:
        dato (dict): diccionario que almacena la clave y su valor
        clave (str): clave donde esta alamacenado el valor
        nombre

    Returns:
        iniciales(str), bandera(bool): tupla que alamacena el str
        de las iniciales y la bandera que valida la obtencion
        de iniciales
    """
    if clave not in dato and dato[clave] != "":
        bandera = False
    
    else:
        iniciales = obtener_inciales(dato[clave])

        bandera = True

    return iniciales, bandera

def obtener_inciales(nombre: str):
    
    if "the" in nombre:
        nombre = nombre.replace("the", "")
    
    if "-" in nombre:
        nombre = nombre.replace("-", " ")
    
    iniciales = ""
    
    # for x,letra in enumerate(nombre):  
    #     if letra.isalpha() and letra != " ":
    #         if x == 0 or nombre[x - 1] == " ":
    #             iniciales += letra.upper() + "."

    #     elif not letra.isspace():

    #         break

    recorrido = 0 #validacion del primer almacenamiento realizado

    for x in nombre:  
        if x.isalpha() and x != " ":
            if recorrido == 0 or valor == " ":
                recorrido += 1

                iniciales += x.upper() + "."

        valor = x #caracter anterior

    return iniciales

# 1.2 y 1.3---------------------------------------------------------------

def agregar_iniciales_nombre(datos: list, clave:str, clave_agregada: str):
    """agrega la clave y su valor a los diccionarios

    Args:
        datos (list): lista que almacena los diccionarios
        al que se agregaran las nuevas claves
        clave (str): clave donde se busca el valor del nombre
        clave_agregada (str): clave donde se almacenara el valor 
        de las iniciales

    Returns:
        datos(list): lista con la clave agregada y su predeterminado valor
    """

    if datos != []:
        for dato in datos:
            iniciales, bandera = definir_iniciales_nombre(dato, clave)

            if bandera:
                dato[clave_agregada] = iniciales

            else:
                print("El origen de datos no contiene el formato correcto")

    return datos


def definir_iniciales_nombre(dato: dict, clave: str):

    iniciales, bandera = extraer_iniciales(dato, clave)

    return iniciales, bandera

# 1.4 ---------------------------------

def stark_imprimir_nombres_con_iniciales(datos: list):
    """recorre la nueva lista creada con la nueva clave
    creada y su valor correspondiente

    Args:
        datos (list): lista que almacena los diccionarios
        al que se agregaran las nuevas claves
    """
    clave_agregada = "iniciales"

    clave = "nombre"

    lista = agregar_iniciales_nombre(datos, clave, clave_agregada)

    for dato in lista:
        if clave_agregada in dato:
            print(f"*{dato[clave]}: {dato[clave_agregada]}")

    return lista

# 2.1 ----------------------------------------------

def generar_codigo_heroe(numero_identificacion: str, genero_heroe: str):
    valor_id = ""

    if genero_heroe == "F" or genero_heroe == "M":
        valor_id = valor_id.join([genero_heroe, "-", numero_identificacion.zfill(8)])

    elif genero_heroe == "NB":
        valor_id = valor_id.join([genero_heroe, "-", numero_identificacion.zfill(7)])
    
    else:
        valor_id = "N/A"

    return valor_id

# 2.2 ------------------------------------------------

def agregar_codigo_heroe(dato: dict, id_heroe: str):
    clave = "codigo_heroe"

    bandera = False

    if dato != {} :
        if len(id_heroe) == 10:
            dato[clave] = id_heroe 

            bandera = True

    return bandera, dato

# 2.3 --------------------------------------------------

def stark_generar_codigos_heroes(datos: list):
    """generena codigos en la lista como una nueva
    clave y su valor correspondiente

    Args:
        datos (list): lista donde agregar los codigos

    Returns:
        bandera, datos (tuple: bool, list): bandera que valida el agregado de 
        los codigos en la lista, y lista con los codigos generados
    """
    clave = "genero"

    recorrido_de_datos = 0

    if datos != []:
        for dato in datos:
            if clave in dato and dato[clave] != "":
                recorrido_de_datos += 1

                valor_id = generar_codigo_heroe(str(recorrido_de_datos), dato[clave])

                bandera, dato = agregar_codigo_heroe(dato, valor_id)

            else:
                print("El diccionario no contiene el formato correcto")
    else:
        print("El origen de datos no contiene el formato correcto")
    
    if recorrido_de_datos != 0:
        print(f"Se asignaron {recorrido_de_datos} codigos")
    
    if "codigo_heroe" in datos[0]:
        print(f"El codigo del primer heroe es:      {datos[0]['codigo_heroe']}")
    
    if "codigo_heroe" in datos[recorrido_de_datos - 1]:
        print(f"El codigo del ultimo heroe es:      {datos[recorrido_de_datos - 1]['codigo_heroe']}")
    
    return bandera, datos
# 3.1-------------------------------------------------

def sanitizar_int(numero_str: str):
    """retorno el valor del string devuelto
    y convertido en entero

    Args:
        numero_str (str): string con valores numericos

    Returns:
        retorno: el valor del numero entero 
        convertido
    """
    import re

    if type(numero_str) == str:
        if " " in numero_str:
            numero_str = re.sub(r"\s+", "", numero_str)

        validacion = re.findall("(^-?[0-9]+$)", numero_str)

        if validacion != []:
            if int(numero_str) > 0:
                retorno = int(numero_str)

            else:
                retorno = -2

        else:
            retorno = -1

    else:
        retorno = -3

    return retorno

# 3.2 -------------------------------------------

def sanitizar_float(numero_str: str):
    """retorno el valor del string
    convertido en flotante

    Args:
        numero_str (str): string que contiene los 
        valores numericos del flotante

    Returns:
        retorno: el valor del numero flotante 
        convertido
    """
    import re

    if type(numero_str) == str:
        if " " in numero_str:
            numero_str = re.sub(r"\s+", "", numero_str)

        validacion = re.findall("(^-?[0-9]+)(.?[0-9]+)", numero_str)

        analisis = re.search("([a-z]?)([A-Z])", numero_str)
        #validacion = re.findall("-[0-9]+.[0-9]+", numero_str)

        if validacion != [] and analisis == None:
            if float(numero_str) > 0:
                retorno = float(numero_str)

            else:
                retorno = -2

        else:
            retorno = -1

    else:
        retorno = -3

    return retorno

# 3.3 -----------------------------------------

def sanitizar_str(valor_str: str):
    """retorno el valor string validado

    Args:
        valor_str (str): el string a validar

    Returns:
        _type_: _description_
    """
    import re 

    valor_str = re.sub("[^\s]\s$", "", valor_str)

    validacion = re.search("[0-9+]", valor_str)

    if validacion == None and valor_str != "":
        if "/" in valor_str:
            valor_str = re.sub("/", " ", valor_str)

        retorno = valor_str.lower()

    else:
        retorno = "N/A"

    return retorno

# 3.4 -----------------------------------------------------------

def sanitizar_dato(heroe: dict, clave: any, tipo_dato: str):
    """recibe un diccionario y normaliza los datos
    segun las claves recibidas

    Args:
        heroe (dict): heroe que almacena los valores
        que se deseen normalizar
        clave (any): clave de diccionario
        tipo_dato (type): tipo de valor al que pertenece
        el dato (str, int, float)

    Returns:
        heroe, bandera: heroe con dato normalizado y bandera
        que verifica que existe ese dato
    """
    import re

    bandera = False

    clave_dict = clave

    match(tipo_dato):
        case "str":
            if clave in heroe:
                valor = sanitizar_str(heroe[clave_dict])

                if valor != "N/A":
                    bandera = True

                    heroe[clave_dict] = valor

            else:
                print(f"la clave {clave} no existe en el heroe")

        case "int":
            if clave in heroe:
                valor = sanitizar_int(heroe[clave_dict])

                bandera = True

                heroe[clave_dict] = valor

            else:
                print(f"la clave {clave_dict} no existe en el heroe")
        case "float":
            if clave in heroe:
                valor = sanitizar_float(heroe[clave_dict])

                bandera = True

                heroe[clave_dict] = valor

            else:
                print(f"la clave {clave_dict} no existe en el heroe")

        case other:
            print("tipo de dato no reconocido")

    return heroe, bandera

# 3.5 -------------------------------------------------------

def stark_normalizar_datos(lista_heroes: list, lista_claves_normalizar: list, lista_datos_normalizar: list):
    """recorre una lista de diccionarios y normaliza los datos
    que alamacena los diccionarios

    Args:
        lista_heroes (list): lista de los diccionaros
        lista_claves_normalizar (list): claves que alamacenan
        los datos a normalizar
        lista_datos_normalizar (list): tipo de dato
    """

    longitud = len(lista_claves_normalizar)

    if lista_heroes != []:

        for heroe in lista_heroes:
            for x in range(longitud):
                heroe_datos_normalizados, bandera = sanitizar_dato(heroe, lista_claves_normalizar[x], lista_datos_normalizar[x])

                heroe = heroe_datos_normalizados

        if bandera:
            print("datos normalizados")

            return lista_heroes, bandera
    
    else:
        print("ERROR: la lista de heroes vacia")

# 4.1 --------------------------------------------------------------

def generar_indice_nombres(lista_heroes: list)-> tuple:
    """genera las partes separadas de los nombres

    Args:
        lista_heroes (list): lista donde se encuentran los nombres

    Returns:
        lista_nombres, bandera (tuple): lista de nombres separadas, bandera que informa
        que la accion fue realizada correctamente
    """
    import re

    clave = "nombre"

    bandera = True

    lista_nombres =  []

    if lista_heroes != []:
        for heroe in lista_heroes:
            if type(heroe) == dict:
                if clave in heroe:
                    indice = re.findall("[A-Z?][a-z]+|\s[a-z]+\s*",heroe[clave])

                    for dato in indice:
                        lista_nombres.append(dato)
                
                else:
                    bandera = False

                    print("El origen de datos no contiene el formato correcto")

                    break
    
    
    return lista_nombres, bandera

# 4.2 -----------------------------------------------------------------------

def stark_imprimir_indice_nombre(lista_heroes: list):
    """imprime la serie de nombres y sus partes, separadas por nombre

    Args:
        lista_heroes (list): lista donde se obtienen los nombres
    """

    lista_indices, bandera = generar_indice_nombres(lista_heroes)

    if bandera:
        cadena_union = "-"

        for x in range(len(lista_indices)):
            if " " in lista_indices[x]:
                lista_indices[x] = lista_indices[x].replace(" ", "")

        impresion = cadena_union.join(lista_indices)

        print(impresion)

# 5.1 ----------------------------------------------------------------------

def convertir_cm_a_mtrs(valor_cm: str or float):
    """convierte el valor de centimetros a metros

    Args:
        valor_cm (str): valor en centimetros

    Returns:
        valor_convertido (float): valor pasado a metros 
    """
    import re

    if type(valor_cm) == str:
        validacion = re.findall("(^-?[0-9]+)(.?[0-9]+)", valor_cm)

        analisis = re.search("([a-z]?)([A-Z])", valor_cm)

        if validacion == [] and analisis == None:
            if float(valor_cm) > 0:
                valor = float(valor_cm)

                valor_convertido = valor / 100

                return valor_convertido
    
    if type(valor_cm) == float:
        if valor_cm > 0:
            valor_convertido = valor_cm / 100

            return valor_convertido
    
    else:
        print("datos no validos")
        return "N/A"


# 5.2 ------------------------------------------------

def generar_separador(patron: str, largo: int, imprimir = True) -> str:
    """genera un separador

    Args:
        patron (str): patron que se va a 
        utilizar para el separador
        largo (int): cantidad de caracteres a crear para el separador
        imprimir (bool, optional): determina si se imprime o no
        el separador. Defaults to True.

    Returns:
        separador (str): separador generado
    """

    if (len(patron) == 1 or len(patron) == 2) and (largo >= 1 and largo <= 235):
        
        separador = patron * largo

    else:
        return "N/A"
    
    if imprimir:
            print(separador)    

    return separador

# 5.3 ------------------------------------------------------

def generar_encabezado(titulo: str):

    titulo = titulo.upper()

    separador = generar_separador("-", 50, False)
    
    titulo_creado = f"""{separador}

{titulo}

{separador}"""

    print(titulo_creado)
    

# 5.4 ---------------------------------------------------------

def imprimir_ficha_heroe(heroe: dict)-> None:
    """imprime la ficha con la informacion general
    del heroe

    Args:
        heroe (dict): heroe a mostrar su informacion
    """
    titulos = ["principal", "fisico", "señas particulares"]

    lista_claves = []

    for valor in range(len(titulos)):
        match(valor):
            case 0:
                generar_encabezado(titulos[valor])

                for datos in heroe:

                        if datos == "nombre":
                            print(f"{datos.upper()}:                {heroe[datos]}({heroe['iniciales']})\n\n")

                        if datos == "identidad":
                            print(f"{datos.upper()}:             {heroe[datos]}\n\n")

                        if datos == "empresa":
                            print(f"{datos.upper()}:                    {heroe[datos]}s\n\n")

                        if datos == "codigo_heroe":
                            print(f"{datos.upper()}                 {heroe[datos]}\n\n")
                
            case 1:
                generar_encabezado(titulos[valor])

                for datos in heroe:

                    if datos == "altura":
                        print(f"{datos.upper()}:                 {heroe[datos]} Mtrs\n\n")

                    if datos == "peso":
                        print(f"{datos.upper()}:                 {heroe[datos]} Kgs\n\n")

                    if datos == "fuerza":
                        print(f"{datos.upper()}                    {heroe[datos]} NT\n\n")
                
            case 2:

                generar_encabezado(titulos[valor])

                for datos in heroe:
                    if (datos == "color_pelo" or datos == "color_ojos"):
                        print(f"{datos.upper()}:               {heroe[datos]}\n\n") 

# 5.5 ---------------------------------------------------------------

def stark_navegar_fichas(lista_heroes: list)-> None:
    import os

    lista_general = agregar_iniciales_nombre(lista_heroes, "nombre", "iniciales")

    contador_externo = 0

    imprimir_ficha_heroe(lista_general[contador_externo])
    
    cantidad_elementos = len(lista_heroes) - 1

    cantidad_elementos2 = -(cantidad_elementos)

    while True:
        
        eleccion = input("""1: heroe en la pocision anterior en la lista

2: heroe en la pocision siguiente en la lista

S: volver al menu principal

Ingrese la opcion deseada:""")

        os.system("cls")

        match(eleccion):
            case "1":
                if contador_externo < cantidad_elementos and contador_externo > cantidad_elementos2:
                    contador_externo = contador_externo - 1

                    imprimir_ficha_heroe(lista_general[contador_externo])

                else:
                    contador_externo = 0

                    imprimir_ficha_heroe(lista_general[contador_externo])

            case "2":
                if contador_externo > cantidad_elementos2 and contador_externo < cantidad_elementos:
                    contador_externo = contador_externo + 1

                    imprimir_ficha_heroe(lista_general[contador_externo])
                
                else:
                    contador_externo = 0

                    imprimir_ficha_heroe(lista_general[contador_externo])

            case "S":
                break
            case other:

                print("ERROR: ingresar un valor valido")

# 6.1 --------------------------------------------------------------

def imprimir_menu():
    print("""
---------------------------------------------------
                    MENU
---------------------------------------------------

1 - Imprimir la lista de nombres junto con sus iniciales

2 - Generar codigo de heroes

3 - Normalizar datos

4 - Imprimir indice de nombres

5 - navegar fichas

S - salir""")

# 6.2 ------------------------------------------------------------------

def stark_menu_principal():
    """valida la opcion seleccionada

    Returns:
        opcion_seleccionada: opcion ya validad
    """
    import os

    while True:
        imprimir_menu()

        opcion_seleccionada = input("seleccione la opcion deseada: ")

        match(opcion_seleccionada):
            case "1":
                break

            case "2":
                break

            case "3":
                break

            case "4":
                break

            case "5":
                break

            case "S":
                break

            case other:
                os.system("cls")
                print("La opcion ingresada no valida")

    return opcion_seleccionada

# 6.4 ----------------------------------------------------------------------

def stark_marvel_app_3(lista_heroes: list):
    import os
    bandera = False

    bandera_cod = False

    validacion2 = True

    validacion3 = True

    while True:
        opt = stark_menu_principal()

        if opt == "1":
            os.system("cls")

            print("La opcion seleccionada fue 1\n---------------------------------------")

            lista_heroes = stark_imprimir_nombres_con_iniciales(lista_heroes)
        
        elif opt == "2":
            os.system("cls")
            if bandera:
                if validacion2:

                    validacion2 = False

                    print("La opcion seleccionada fue 2\n---------------------------------------")

                    bandera_cod, lista_heroes = stark_generar_codigos_heroes(lista_heroes)

                else:
                    print("codigos ya agregados")

            else:
                print("valida los datos primero")

        elif opt == "3":
            os.system("cls")
            if validacion3:
                print("La opcion seleccionada fue 3\n---------------------------------------")
                
                lista_heroes, bandera = stark_normalizar_datos(lista_heroes, ["altura", "peso", "fuerza", "color_ojos", "color_pelo"], ["float", "float", "int", "str", "str"])

                validacion3 = False

            else:
                print("datos ya normalizados")
        elif opt == "4":
            os.system("cls")

            print("La opcion seleccionada fue 4\n---------------------------------------")

            stark_imprimir_indice_nombre(lista_heroes)

        elif opt == "5":
            os.system("cls")
            if bandera and bandera_cod:
                for heroe in lista_heroes:
                    heroe["altura"] = convertir_cm_a_mtrs(heroe["altura"])

                stark_navegar_fichas(lista_heroes)

            else:
                print("ERROR\nnormalice los datos primero\ngenere los codigos de los heroes\n--------------------------")

        elif opt == "S":
            os.system("cls")

            print("La opcion seleccionada fue 4\n---------------------------------------")

            print("ADIOS")

            break






