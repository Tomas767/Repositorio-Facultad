# import re
# import os
# import json

# letra = "tetitas marsupia"

# palabras = re.findall("[a-z]+", letra)



# print(palabras)
# valor = "celeste"
# import re

# retorno = re.findall("^[\s]", valor)

# if retorno == [] and valor != "":
#     print("tiene caraacteres")

# else:
#     print("esta vacio")

# diccionario = {"Nombre": "pepito"
#                ,"color_ojos": "Azul"}

# if "color_ojos" in diccionario:
#     print(True)

# from funciones_main5 import *


# heroes = leer_archivo()

# print(heroes)
import re

str = "Tetas"

str = str.lower()

palabras = re.findall("[a-z]+-?[a-z]+|[a-z]+\s[a-z]+", str)

if palabras != []:
    if type(palabras) == list:
        for i in range(len(palabras)):
            palabras[i] = palabras[i].capitalize()

        palabra_capitalizada = " ".join(palabras)

print(palabra_capitalizada)

