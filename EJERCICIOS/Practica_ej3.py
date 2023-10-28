repeticiones = 0

cont_pares = 0
cont_inpares = 0

flag1 = True

flag2 = True

acomulador_post = 0

num_negativos = []
producto_neg = 0

while True:
    numero = int(input("ingrese un numero: "))

    if numero != 0:
        repeticiones += 1

        if numero % 2 == 0:
            cont_pares += 1

            if flag2:
                par_mayor = numero

                flag2 = False

            else:
                if par_mayor < numero:

                    par_mayor = numero

        else: 
            cont_inpares += 1

        if flag1: 
            num_menor = numero

            flag1 = False

        elif num_menor > numero:
            num_menor = numero

        if numero > 0:
            acomulador_post += numero

        else:
            num_negativos.append(numero)

    else:
        print("numero debe ser mayor a cero")
    
    if repeticiones == 5:
        break

for x in num_negativos:
    producto_neg = x


print(f"""la cantidad de pares son: {cont_pares}
impares son: {cont_inpares}""")
print(f"el menor numero ingresado es: {num_menor}")
print(f"el numero par mayor es: {par_mayor}")
print(f"la suma de los positivos es: {acomulador_post}")
print(f"el producto de los negativos es: {producto_neg}")