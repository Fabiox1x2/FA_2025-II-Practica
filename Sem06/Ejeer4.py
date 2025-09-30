g=input("genere una contraseña")
print("---------------------------------")
print("       VALIDA TU CONTRASEÑA")
print("                                 ")
print("       ud. tiene 3 intentos ")
print("-------------------------------\n")

intentos=3

while(intentos>0):
    c=input("ingrese la contraseña")
    if g==c :
        print("\ACCESO CONCEDIDO. BIENVENIDO AL SISTEMA. ")
    else:
        intentos -=1
        print("CONTRASEÑA INCORRECTA. INTENTOS RESTANTES ", intentos)

else: print("ACCESO DENEGADO! CERRANDO SISTEMA")