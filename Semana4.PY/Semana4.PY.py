from pprint import PrettyPrinter


def ejer1():
    edad= int(input("Ingrese una edad: "))

    if edad<18:
        print("menor de edad")
    else: 
        if edad>=18 and edad<=64:
            print("Adulto")
        else:
            print("adulto mayor")




def ejerc2():

  lado1 = int(input("Ingrese lado1: "))

  lado2 = int(input("Ingrese lado2: "))

  lado3 = int(input("Ingrese lado3: "))



  if (lado1 == lado2 == lado3):

    print ("EQUILATERO")

  elif lado1 == lado2 or lado1 ==lado3 or lado2 == lado3:

    print ("ISOCELES")

  else:

    print ("ESCALENO")
   
    
def ejer3():
        n=int(input("ingrese un numero: "))

        print()
        for i in range (1,n+1):
            print(i)

            if i % 2 ==0:
                suma += i

                print("/nSuma de pares: ", suma)

def ejer4():
    cant=int(input("ingrese la cantidad de numeros: "))
    ceros = pares = impares=0
    print()
    for i in range(1, cant+1):
        num=int(input(f"ingrese el numero {i}:"))

        if num ==0:
            ceros+=1 # ceros++
        elif num % 2==0:
            pares+=1 #pares++
        else:
            impares +=1 #impares++

    print("\n#ceros: ", ceros)
    print("#pares: ", pares)
    print("#impares: ",impares)
            
        


ejer4()

