#coding: utf8 
#Pau Martín Fernandez
import os
numero=1 
maximo=8
vueltas=input ("Cuantas vueltas quieres?: ") 
giro=raw_input ("Hacia donde giro? Porfavor, pongalo en mayusculas.")
salir="N"
while(salir=="N"): 
    if(numero%8==1) or (numero%8==2): 
        print ( numero,"Arriba") 
    if(numero%8==3) or (numero%8==4): 
        if(giro=="D"):
            print ( numero,"Derecha")
        else:
			print (numero,"Izquierda")     
    if(numero%8==5) or (numero%8==6): 
        print ( numero,"Abajo") 
    if(numero%8==7) or (numero%8==0):
		if(giro=="D"):
			print (numero, "Izquierda")
		else:
			 print ( numero,"Derecha") 	
    
    numero = numero + 1
    if(numero > vueltas * maximo): 
        salir = "S"

