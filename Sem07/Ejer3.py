suma=0
while True:
    num= int(input("ingrese un numero positivo: "))


    for i in range(1,num+1):
        suma+=i
        print(i, end=" ")

    print("\nSuma: ", suma)
    opc = input("\n¿desea continuar?(S/N) :")

    if(opc =="N"): break
