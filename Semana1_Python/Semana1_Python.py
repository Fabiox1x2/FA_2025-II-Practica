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

ejer2()