# coding: utf8
# Pau Martín Fernández
salir = " N "
numero=1
maximo=5
suma=0
while ( salir=="N" ):
    # Hago cosas
    print (numero ,)
    if(numero<=maximo-1):
        print (" + " ,)
	
    suma=suma+numero
    numero=numero+1
    if ( numero > maximo ): # Condición de salida
            salir = " S "
print (" = " , suma) 
