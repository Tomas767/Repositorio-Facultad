while True:

    edad = input("ingrese una edad: ")

    if edad.isnumeric():

        edad = int(edad)

        if edad > 0 and edad < 100:

            break

if edad > 17:

    print("usted es mayor de edad")

elif edad > 13 and edad < 18:

    print("usted es adolecente")

else:

    print("usted es un niño")


