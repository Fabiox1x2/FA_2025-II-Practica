sumap= sumai=0
while True:
    num = int(input("ingrese un numero (0 salir): "))
    
    if num<0:
        print("numero invalido. Ingrese nuevamente")

        continue 
    if num ==0:
        break
    if num%2 ==0:
        sumap+=num
    else:
        sumai +=num
print("\nSuma de pares: ", sumap)
print ("suma de impares: ", sumai)