def ejer1():#creando metodo ejer1
    nombre= input("ingrese su nombre")
    carrera= input("ingrese su carrera")

    print(f"\n{nombre}, bienvenido a FA de {carrera}")

    def ejer2():
    x= int(input("ingrese el valor de x: "))
    y= int(input("Ingrese el valor de y: "))

    print("Suma: ", (x+y))
    print("Resta: ",(x-y))
    print("Multiplicacion: ", (x*y))
    print("Division: ", (x/y))


import math #importando la libreria math
def ejer4():
    num= float(input("ingrese un numero decimal: "))
    print("raiz 2: ", math.sqrt(num))
    print("redondeando: ", round(num, 0))
    print("al cubo: ", math.pow(num,3))
    print("raiz 3", num ** (1/3))
ejer4()

def ejer5():
    num= input("ingrese numero: ")

    entero= int(num)
    deci= float(num)

    print("Resto: ", (entero%2))
    print("Division: ", (deci/3))

ejer5()