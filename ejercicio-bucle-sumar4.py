# coding: utf8
# Pau Martín Fernández
salir = " N "
numero=1
maximo=5
suma=0
while ( salir=="N" ):
    if(numero%2==0):
        print (numero ,)
        if(numero<=maximo-2):
            print (" + " ,)
	
        suma=suma+numero
        
    numero=numero+1
    if ( numero > maximo ): 
            salir = "S"
print (" = " , suma)
