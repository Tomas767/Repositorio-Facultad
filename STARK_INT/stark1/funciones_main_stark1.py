def menu():
    import os

    while True:
        op = input("""
                    MENU
--------------------------------------------
favor de escribir unicamente 
el numero para seleccionar
la opcion
--------------------------------------------
1ra opcion: recorrer la lista de superheroes
                   
2da opcion: mostrar identidad y peso del superheroe mas fuerte
                   
3ra opcion: mostrar nombre e identidad del superheroe mas bajo(altura)
                   
4ta opcion: mostrar promedio de la altura de los superheroes masculinos
                   
5ta opcion: Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino

opcion deseada: """)
        
        match(op):
            case "1ra":
                break
            
            case "2da":
                break

            case "3ra":
                break

            case "4ta":
                break

            case "5ta":
                break

            case other:
                print("descripcion no valida")

                os.system("pause")

                os.system("cls")
        
        break

    return op

def ordenar_datos(datos: list):
    """recorre la lista de diccionarios y
    mediante una serie de iteraciones ordena por
    clave valor mustra la lista iterada

    Args:
        datos (list): lista que almacena los datos
        que se desea iterar
    """
    for dato in datos:
        for clave, valor in dato.items():#items() devuelve una tupla de tanto la clave
            print(f"{clave}: {valor}")     # como su valor para utilizarlo de manera conveniente
        print("-------------------------------------------")

def maximos(datos: list, indicador: any, elemento: any, elemento2: any):
    """recorre los datos de una lista de diccionarios
    para recorrer los elementos, determinando cual es el maximo 
    basandose en un indicador

    Args:
        datos (list): lista de diccionarios
        indicador (any): clave donde se almacena el valor a comparar
        para determinar
        elemento (any): clave donde se almacena el valor que se desea resaltar
        de segun el programa
        elemento2 (any): clave donde se almacena el segundo valor que se desea resaltar
        de segun el programa

    Returns:
        tupla: devuelve las listas de los maximos en
        en caso de que dos o mas elementos tengan el mismo
        valor maximo
    """
    flag_max = True

    maximo_x = []#donde se almacena la indentidad

    maximo_x2 = []#donde se alamacena el peso

    for dato in datos:
        for clave, valor in dato.items():
            x = dato[elemento]
            

            x2 = dato[elemento2]

            if clave == indicador:
                valor = float(valor)

                if flag_max:
                    maximo = valor

                    a = x

                    maximo_x.append(x)

                    b = x2  

                    maximo_x2.append(x2)
                    
                    flag_max = False

                elif valor > maximo:
                    maximo = valor

                    index = maximo_x.index(a)

                    a = x

                    maximo_x[index] = x

                    index2 = maximo_x2.index(b)

                    b = x2

                    maximo_x2[index2] = x2

    for dato in datos:
        for clave2, valor2 in dato.items():
            y = dato[elemento]

            y2 = dato[elemento2]

            if clave2 == indicador:
                valor2 = float(valor2)

                for element in maximo_x:
                    if y != element:
                        if valor2 == maximo:
                            maximo_x.append(y)

                            maximo_x2.append(y2)


    return maximo_x, maximo_x2

def minimo(datos: list, indicador: any, elemento: any, elemento2: any ):
    """recorre los datos de una lista de diccionarios
    para recorrer los elementos, determinando cual es el minimo 
    basandose en un indicador

    Args:
        datos (list): lista de diccionarios
        indicador (any): clave donde se almacena el valor a comparar
        para determinar
        elemento (any): clave donde se almacena el valor que se desea resaltar
        de segun el programa
        elemento2 (any): clave donde se almacena el segundo valor que se desea resaltar
        de segun el programa
    
    return:
        tupla: devuelve las listas de los maximos en
        en caso de que dos o mas elementos tengan el mismo
        valor maximo
    """
    flag_min = True

    minimo_x = []#donde se almacena el nombre

    minimo_x2 = []#donde se alamacena la identidad
    for dato in datos:
        for clave, valor in dato.items():
            x = dato[elemento]
            

            x2 = dato[elemento2]

            if clave == indicador:
                valor = float(valor)

                if flag_min:
                    minimo = valor

                    a = x

                    minimo_x.append(x)

                    b = x2  

                    minimo_x2.append(x2)
                    
                    flag_min = False

                elif valor < minimo:
                    minimo = valor

                    index = minimo_x.index(a)

                    a = x

                    minimo_x[index] = x

                    index2 = minimo_x2.index(b)

                    b = x2

                    minimo_x2[index2] = x2

    for dato in datos:
        for clave2, valor2 in dato.items():
            y = dato[elemento]

            y2 = dato[elemento2]

            if clave2 == indicador:
                valor2 = float(valor2)

                for element in minimo_x:
                    if y != element:
                        if valor2 == minimo:
                            minimo_x.append(y)

                            minimo_x2.append(y2)

    return minimo_x, minimo_x2

def promedio(datos: list, indicadador: any, elemento: any):
    count = 0    
    
    accomulator = 0
    
    for data in datos:
        count += 1

        for clave, valor in data.items():
            if valor == indicadador:
                valor = float(data[elemento])
                
                accomulator += valor
    
    if count != 0 and accomulator != 0:
        promedio = accomulator / count
    else:
        promedio = "no se produjo ningun promedio"

    return promedio

def mayor(datos: list, comparador: int, indicador: int, elemento: str, elemento2: str):
    list_elements = []

    list_elements2 = []

    for dato in datos:
        for clave, valor in dato.items():
            if clave == indicador:
                valor = float(valor)
                if valor > comparador:
                    
                    list_elements.append(dato[elemento])

                    list_elements2.append(dato[elemento2])

    return list_elements, list_elements2