
# 0----------------------------------------------
def stark_normalizar_datos(datos: list)-> bool and list:
    import re

    datos_normalizados = []

    bandera_1 = False

    for dato in datos:
        for clave, valor in dato.items():
            if type(valor) != float and type(valor) != int:

                match = re.findall("([0-9]+.?[0-9]+)", valor)
                #() todo un grupo
                #[0-9]+ todos lo elementos disponibles en ese rengo de valores
                #.? ninguno o algun punto
                for elemento in match:
                    if elemento.isnumeric():
                        #print(elemento)
                        numero = int(elemento)
                    else:
                        #print(elemento)
                        numero = float(elemento)
                    
                    dato[clave] = numero

                bandera_1 = True

        datos_normalizados.append(dato)

    if bandera_1:
        print("datos nomalizados")

        return datos_normalizados, bandera_1
    else:
        print("""Hubo un error al normalizar los datos. Verifique que la lista no este
vacía o que los datos ya no se hayan normalizado anteriormente""")
        return datos_normalizados, bandera_1
    

# 1.1 y 1.2-------------------------------------------
def obtener_dato(dato: dict, cualidad: str)-> bool:
    """recorre un diccionario iterando por
    clave: valor segun se desee

    Args:
        dato (dict): diccionario que almacena datos
        cualidad (str): nombre de la clave que se desea 
        imprimir

    Returns:
        bandera_2: bandera que determina si hay o no
        elementos dentro de las claves
    """
    bandera_2 = True

    if dato != {}:
        for clave, valor in dato.items():
            if cualidad == clave:
                if valor != " ":
                    bandera_2 = False

                    clave = clave.capitalize()

                    valor = valor.capitalize()

                    print(f"{clave}: {valor}") 

                else: 
                    print("el valor de la clave esta vacio")

    return bandera_2

# 2------------------------------------
def obtener_nombre_y_dato(diccionario: dict, elemento: str, dato: str)-> str and bool:
    """recibe el diccionario donde se almacenan los datos
    y segun el elemento que tenga el mismo valor recibido
    se retorna el dato determinado

    Args:
        diccionario (dict): diccionario donde se alamacenan los datos
        elemento (str): donde se almacena y destaca el dato
        que buscamos
        dato (str): dato a resaltar

    Returns:
        str and bool: el dato deseado, la clave donde se almacena el valor,
        el valor de la clave y la bandera que determina si se encontro
        o no el dato que se busca
    """
    bandera_3 = False

    dato_deseado = None

    if diccionario != {}:
        for clave, valor in diccionario.items():
            if elemento == valor:
                if valor != "":
                    bandera_3 = True

                    dato_deseado = diccionario[dato]

                    print(diccionario[dato])

                    clave1 = clave.capitalize()

                    valor1 = valor.capitalize()

                    print(valor)
                    break

                else: 
                    print("el valor de la clave esta vacio")

    return dato_deseado, clave1, valor1, bandera_3

# 3.1 y 3.2-------------------------------------------
def maximo_minimo(datos: list, analisis: str,indicador: str)-> (float or int) and bool:
    """determina el analisis al que se quiere proceder segun si se quiere
    el maximo valor o el minimo, y 

    Args:
        datos (list): lista donde se almacena los diccionarios y los
        datos que se van a recorrer
        analisis (str): determinante que permite el analisis en caso de
        que se busque un maximo o un minimo
        indicador (str): valor a analizar para determinar
        maximos y minimos

    Returns:
        list: lista de elementos destacados 
    """
    flag_max_min = True

    flag_validacion = False

    max_min_x = None

    if analisis == "minimo":
        for dato in datos:
            for clave, valor in dato.items():                
                if clave == indicador:
                    if type(valor) == float or type(valor) == int:
                        if flag_max_min:
                            max_min_x = valor

                            flag_max_min = False

                            flag_validacion = True

                        elif valor < max_min_x:
                            max_min_x = valor

    elif analisis == "maximo":
        for dato in datos:
            for clave, valor in dato.items():
                if clave == indicador:
                    valor = float(valor)

                    if flag_max_min:
                        max_min_x = valor

                        flag_max_min = False

                        flag_validacion = True

                    elif valor > max_min_x:
                        max_min_x = valor

    return max_min_x, flag_validacion

# 3.3------------------------------------------
def obtener_dato_cantidad(datos: list, analisis: str,indicador: str)-> (list) and bool:
    """determina el analisis al que se quiere proceder segun si se quiere
    el maximo valor o el minimo, y recorre los diccionarios almacenados en una lista
    para asi obtener los valores maximos o minimos segun se desee

    Args:
        datos (list): lista donde se almacena los diccionarios y los
        datos que se van a recorrer
        analisis (str): determinante que permite el analisis
        indicador (str): valor a analizar para determinar
        los datos que se van a recorrer

    Returns:
        list and bool: lista de valores destacados y booleano 
        que determina si se comparo y encontro el valor
        buscado
    """
    flag_dato = True

    flag_validacion = False

    elemento = {}

    lista_elementos = []

    if analisis == "minimo":
        for dato in datos:
            for clave, valor in dato.items():                
                if clave == indicador:
                    if type(valor) == float or type(valor) == int:
                        if flag_dato:
                            elemento = dato

                            lista_elementos.append(elemento)

                            index = lista_elementos.index(elemento)

                            flag_dato = False

                            flag_validacion = True

                        elif dato[indicador] < elemento[indicador]:
                            elemento = dato

                            lista_elementos[index] = elemento
        
        for dato in datos:
            if type(dato[indicador]) == float or type(dato[indicador]) == int:
                if dato[indicador] == elemento[indicador] and dato not in lista_elementos:
                    lista_elementos.append(dato)
                    

    elif analisis == "maximo":
        for dato in datos:
            for clave, valor in dato.items():                
                if clave == indicador:
                    if type(valor) == float or type(valor) == int:
                        if flag_dato:
                            elemento = dato

                            lista_elementos.append(elemento)

                            index = lista_elementos.index(elemento)

                            flag_dato = False

                            flag_validacion = True

                        elif dato[indicador] > elemento[indicador]:
                            elemento = dato

                            lista_elementos[index] = elemento
        
        for dato in datos:
            if type(dato[indicador]) == float or type(dato[indicador]) == int:
                if dato[indicador] == elemento[indicador] and dato not in lista_elementos:
                    lista_elementos.append(dato)

    return lista_elementos, flag_validacion

# 3.4------------------------------------------
def stark_imprimir_heroes(datos: list, condicon_opcional = None)-> None:
    """recibe una lista de datos la cual se va a recorrer
    e imprimir en caso de que no exista condicion recorre toda la 
    lista, en caso contrario recorre un grupo particular

    Args:
        datos (list): datos donde se almacenan los 
        elementos a imprimir
        condicional_opcional (None): condicon de valor en un clave
        que permite el analsis particular de unicamente
        ciertos elementos en la lista
    """
    lista_claves = []

    bandera = False

    if condicon_opcional == None:
        if datos != []:
            for dato in datos:
                for clave in dato:
                    if clave not in lista_claves:
                        lista_claves.append(clave)

            for dato in datos:
                for clave in lista_claves:
                    print(f"{clave}: {dato[clave]}")

                print("-------------")

        else:
            print(f"la lista registrada se encuentra vacia")

    else:
        if datos != []:
            for dato in datos:
                for clave in dato:
                    if clave not in lista_claves:
                        lista_claves.append(clave)

            for dato in datos:
                if condicon_opcional in dato:
                    bandera = True
                    for clave in lista_claves:
                        if dato[clave] == condicon_opcional:
                            print(f"{clave}: {dato[clave]}")
                    print("-------------")
            
            if not bandera:
                print(F"NO EXISTE NIGNUN VALOR {condicon_opcional}")
        
        else:
            print(f"la lista registrada esta vacia")
            

# 4.1-------------------------------------------

def sumar_dato(datos: list, clave: str, condicional_opcional = None, condicion_opcional = None)-> (int or float):
    """recorre la lista recibida y analiza para acomular los valores almacenados en los
    diccionarios generales o especificos en caso de condicion externa

    Args:
        datos (list): lista donde se almacenan los diccionarios que se iteraran
        clave (str): clave de diccionario donde se almacenan los valores
        que se desean sumar 
        condicional_opcional (None, opcional):clave que agrupa 
        determinados valores especificos
        condicion_opcional (None, opcional): valor especifico que agrupa ciertos
        elementos mediante condicional

    Returns:
        int or float: la suma total valores acomulados dentro de la lista
    """
    suma = 0

    if condicion_opcional == None:    
        for dato in datos:
            if dato != {}:
                for elemento in dato:
                    if elemento == clave and (type(dato[elemento]) ==  float or type(dato[elemento]) == int):
                        suma += dato[elemento]
    
    else:
        for dato in datos:
            if dato != {} and dato[condicional_opcional] == condicion_opcional:
                for elemento in dato:
                    if elemento == clave and (type(dato[elemento]) ==  float or type(dato[elemento]) == int):
                        suma += dato[elemento]
    
    return suma

# 4.2-------------------------------------------   

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

# 4.3------------------------------------------

def sacar_promedio(datos: list, clave:str, condicional_opcional = None, condicion_opcional = None) -> (int or float):
    """a traves de la lista recibida y la clave donde se almacena los valores que se desean
    calcular su promedio suma los valores y la cantidad de diccionarios que poseen
    el mismo para asi sacar el promedio

    Args:
        datos (list): lista donde se almacenan los diccionarios que se iteraran
        clave (str): clave de diccionario donde se almacenan los valores
        que se desean sumar 
        condicional_opcional (None, opcional):clave que agrupa 
        determinados valores especificos
        condicion_opcional (None, opcional): valor especifico que agrupa ciertos
        elementos mediante condiciona

    Returns:
        int or float: devuleve el promedio total de los valores encontrados 
        segun cuantos diccionarios lo poseean
    """
    contador = 0

    promedio = 0

    if condicional_opcional == None:
        suma_datos = sumar_dato(datos, clave)

        for dato in datos:
            for elemento in dato:
                if elemento == clave:
                    contador += 1
    
    elif condicional_opcional != None:
        suma_datos = sumar_dato(datos, clave, condicional_opcional, condicion_opcional)

    promedio, bandera_5= dividir(contador, suma_datos)

    return promedio, bandera_5

# 5.1-------------------------------------------
def imprimir_menu():
    op = input("""
                MENU
--------------------------------------------
favor de escribir unicamente 
el numero para seleccionar
la opcion
--------------------------------------------
1: normalizar datos

2: mostrar nombres de supers

3: mostrar nombre y dato del super seleccionado

4: calcular el maximo

5: calcular el minimo

6: calcular cantidad                   

7: calcular promedio

opcion elegida: """)

    return op

# 5.1------------------------------------------

def validar_entero(entero: str)-> bool:
    """analisa si el str entregado es un valor
    entero

    Args:
        entero (str): str a validar si es o no
        un entero

    Returns:
        bool: False si el str no es entero
        True si el str si es entero
    """
    bandera_8 = False

    if entero.isnumeric():
        bandera_8 = True
    
    return bandera_8

# 5.3-------------------------------------------
def stark_menu_principal()->str:
    import os

    while True:
        op = imprimir_menu()
        
        match(op):
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
            case "6":
                break
            case "7":
                break
            case other:
                print("No existe tal opcion/ seleccione una nueva")

                os.system("pause")

                os.system("cls")

    return op

# 6----------------------------------------------------------------------------------------------

from data import lista_personajes

def stark_marvel_app(datos: list):
    bandera_1 = False

    import os

    while True:
        opcion_deseada = input("""
                    MENU
------------------------------------------
seleccione la opcion deseada poniendo
unicamente las letras que se 
muestran en pantalla (A-k)
-------------------------------------------
A. Normalizar datos 
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
J. Listar todos los superhéroes agrupados por color de ojos.
K. Listar todos los superhéroes agrupados por tipo de inteligencia

opcion deseada: """)
        
        match(opcion_deseada):
            case "A":
                datos, bandera_1 = stark_normalizar_datos(lista_personajes)
            case "B":
                if bandera_1:
                    stark_imprimir_heroes(datos, "NB")
                
                else:
                    print("los datos no fueron normalizados")
            case "C":
                if bandera_1:
                    lista_heroes = maximo_minimo_stark_2(lista_personajes, "maximo", "genero", "F", "altura", "nombre")
                
                    if lista_heroes != []:
                        print(f"los superheroes femenino mas altos son: ")

                        for heroe in lista_heroes:
                            print(f"*{heroe}")
                    
                    else:
                        print("no se genero ningun analisis/ o no existen heroes del genero F en la lista")
                else:
                    print("los datos no fuernos normalizados")
            case "D":
                if bandera_1:
                    lista_heroes = maximo_minimo_stark_2(lista_personajes, "maximo", "genero", "M", "altura", "nombre")
                
                    if lista_heroes != []:
                        print(f"los superheroes masculinos mas altos son: ")

                        for heroe in lista_heroes:
                            print(f"*{heroe}")

                    else:
                        print("no se genero ningun analisis/ o no existen heroes del genero M en la lista")

                else:
                    print("los datos no fueron normalizados")
            case "E":
                if bandera_1:
                    lista_heroes = maximo_minimo_stark_2(lista_personajes, "minimo", "genero", "M", "fuerza", "nombre")

                    if lista_heroes != []:
                        print("el superheroe mas debil del genero M es:")

                        for heroe in lista_heroes:
                            print(heroe)
                    else:
                        print("no se genero ningun analisis/ o no existen heroes del genero M en la lista")
                else:
                    print("los datos no fueron normalizados")
            case "F":
                if bandera_1:
                    lista_heroes = maximo_minimo_stark_2(lista_personajes, "minimo", "genero", "NB", "fuerza", "nombre")

                    if lista_heroes != []:
                        print("el superheroe mas debil del genero NB es:")

                        for heroe in lista_heroes:
                            print(heroe)
                    else:
                        print("no se genero ningun analisis/ o no existen heroes del genero NB en la lista")
                else:
                    print("los datos no fueron normalizados")
            case "G":
                if bandera_1:
                    promedio, bandera_2 = sacar_promedio(datos, "fuerza", "genero", "NB")

                    if bandera_2:
                        print(f"el promedio de la fuerza de los heroes del genero NB es de: {promedio}")
                    
                    else:
                        print("no se genero ningun promedio/ no exite ningun heroe del genero NB")
            case "H":
                if bandera_1:
                    set_elementos = crear_set(lista_personajes, "color_ojos")

                    print("La cantidad de heroes con cada tipo de color de ojos son: ")
                    for elemento in set_elementos:
                        contador = contavilizar(lista_personajes, elemento, "color_ojos")                

                        print(f"""
{elemento}: {contador}""")    
                else:
                    print("no se normalizaron los datos")
            case "I":
                if bandera_1:
                    set_elementos = crear_set(lista_personajes, "color_pelo")

                    print("La cantidad de heroes con cada tipo de color de pelo son: ")
                    for elemento in set_elementos:
                        contador = contavilizar(lista_personajes, elemento, "color_pelo")  

                        print(f"""
{elemento}: {contador}""")              
                else:
                    print("no se normalizaron los datos")
            case "J":
                if bandera_1:
                    set_elementos = crear_set(lista_personajes, "color_ojos")

                    for elemento in set_elementos:
                        recorrer_set(lista_personajes,"color_ojos", elemento, 'nombre')
                else: 
                    print("no se normalizaron los datos")
            case "K":
                if bandera_1:
                    set_elementos = crear_set(lista_personajes, "inteligencia")

                    for elemento in set_elementos:
                        recorrer_set(lista_personajes,"inteligencia", elemento, 'nombre')
                else: 
                    print("no se normalizaron los datos")
            case other:
                print(f"la opcion {opcion_deseada} no esta disponible")
    
        os.system("pause")

#---------------------------------------------------------------------------------------------------------------
def crear_set(datos: list, cualidad: str):
    set_cualidades = []

    for dato in datos:
        for clave, valor in dato.items():
            if clave == cualidad and valor not in set_cualidades:
                set_cualidades.append(valor)

    return set_cualidades

def recorrer_set(datos: list, cualidad: str, elemento: str, descripcion: str):
    set_destacado = []

    for dato in datos:
        for clave, valor in dato.items():
            if clave == cualidad:#color_ojos
                if valor == elemento:#1ro brown
                    set_destacado.append(dato)

    print(f"""
------------------------
{elemento}
------------------------""")
    for x in set_destacado:
        print(f"{x[descripcion]}")

def contavilizar(datos: str ,cualidad: str, clave: str):
    count = 0

    for dato in datos:
        # print(dato[clave] + "-----" + cualidad)
        if cualidad == dato[clave]:
            count += 1
    
    return count

def maximo_minimo_stark_2(datos: list, analisis: str, condicion: str, valor_condicion: str,indicador: str , elemento: str):
    """_summary_

    Args:
        datos (list): lista donde se almacena los diccionarios y los
        datos que se van a recorrer
        analisis (str): determinante que permite el analisis en caso de
        que se busque un maximo o un minimo
        condicion(str): aplica una condicion de los elementos para analizar
        y recorrer unicamente esos elementos en particular
        valor_condicion(str): valor de la clave que establece la condicion
        indicador (str): valor a analizar para determinar
        maximos y minimos
        elemento (str): elementos a destacar y retornar

    Returns:
        list: lista de elementos destacados 
    """
    flag_max_min = True

    max_min_x = []#donde se almacena el nombre

    if analisis == "minimo":
        for dato in datos:
            for clave, valor in dato.items():
                x = dato[elemento]
                
                if dato[condicion] == valor_condicion:
                    if clave == indicador:
                        valor = float(valor)

                        if flag_max_min:
                            maximo_minimo = valor

                            a = x

                            max_min_x.append(x)

                            flag_max_min = False

                        elif valor < maximo_minimo:
                            maximo_minimo = valor

                            index = max_min_x.index(a)

                            a = x

                            max_min_x[index] = x

        for dato in datos:
            for clave2, valor2 in dato.items():
                y = dato[elemento]

                if dato[condicion] == valor:
                    if clave2 == indicador:
                        valor2 = float(valor2)

                    for element in max_min_x:
                        if y != element:
                            if valor2 == maximo_minimo:
                                max_min_x.append(y)

    elif analisis == "maximo":
        for dato in datos:
            for clave, valor in dato.items():
                x = dato[elemento]
                
                if dato[condicion] == valor_condicion:
                    if clave == indicador:
                        valor = float(valor)

                        if flag_max_min:
                            maximo_minimo = valor

                            a = x

                            max_min_x.append(x)

                            flag_max_min = False

                        elif valor > maximo_minimo:
                            maximo_minimo = valor

                            index = max_min_x.index(a)

                            a = x

                            max_min_x[index] = x

        for dato in datos:
            for clave2, valor2 in dato.items():
                y = dato[elemento]

                if dato[condicion] == valor:
                    if clave2 == indicador:
                        valor2 = float(valor2)

                    for element in max_min_x:
                        if y != element:
                            if valor2 == maximo_minimo:
                                max_min_x.append(y)
    return max_min_x
    