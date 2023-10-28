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
A: recorrer la lista mostrando los superheroes 
de genero NB
B: recorrer la lista mostrando el superheroina
mas alto
C: recorrer la lista mostrando la superheroe
mas alto
D: recorrer la lista mostrando el superheroe 
del genero M mas debil
E: recorrer la lista mostrando el superheroe
del genero NB mas debil
F: recorrer la lista y mostrar el promedio de fuerza
de los supers del genero NB
G: mostrar la cantidad de supers que tienen cada
tipo de color de ojos
H: mostrar la cantidad de supers que tienen cada
tipo de color de pelo
I: agrupar heroes por color de ojos
J: agrupar heroes por tipo de inteligencia

opcion elegida: """)
        
        match(op):
            case "A":
                break
            case "B":
                break
            case "C":
                break
            case "D":
                break
            case "E":
                break
            case "F":
                break
            case "G":
                break
            case "H":
                break
            case "I":
                break
            case "J":
                break
            case other:
                print("opcion no valida")
                
        break

    return op

def buscar(datos: list, indicador: str, particularidad: str, elemento: str):
    """recorre la lista diccionario donde se almacenan los datos
    y se almacena y retorna segun una particularidad determinada

    Args:
        datos (list): lista de diccionarios
        indicador (str): clave donde se almacena la particularidad
        particularidad (str): particularidad que se determina la igualdad
        con el valor de la clave
        elemento (str): elemento a destacar
    Returns:
        list: lista donde se almacenaron los elementos
    """
    list_elementos = []

    for dato in datos:
        for clave, valor in dato.items():
            if clave == indicador:
                if valor == particularidad:
                    list_elementos.append(dato[elemento])
    
    return list_elementos

def maximo_minimo(datos: list, analisis: str, condicion: str, valor_condicion: str,indicador: str , elemento: str):
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