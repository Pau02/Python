# coding: utf8
# Pau Martin Fernandez
salir = " N "
numero=1
maximo=5
suma=0
while ( salir=="N" ):
    # Hago cosas
    if(numero%2==0):
        print (numero ,)
    
        suma=suma+numero
    numero=numero+1
    if ( numero > maximo ): # Condición de salida
            salir = "S"
print (" = " , suma) 
