# coding: utf8
# Pau Martín Fernandez
salir = " N "
numero=1
maximo=5
suma=0
while ( salir=="N" ):
    print numero 
   
	
    suma=suma+numero
    numero=numero+1
    if ( numero > maximo ):
            salir = "S"
print "=" , suma 
