#coding: utf8
#Pau Martin Fernandez

import os
os.system ("clear")

print '''
#####################################
Super/Normal=1
Super/Turbo=2
Sin Plomo/Normal=3
Sin Plomo/Con Aditivo=4
Diesel/Normal=5
Diesel/Fast&Furius=6
#####################################
'''

gasolina=input("Que Gasolina Desea Señor?")
litros=input("Cuantos Litros quieres?")

if (gasolina==1):
	print "Has elegido Super Normal! Son 1.5 por litro!", (litros*1.5) ,"€"
if (gasolina==2):
	print "Has elegido Super Turbo! Son 1.55 por litro!", (litros*1.55),"€"
if (gasolina==3):
	print "Has elegido Sin Plomo Normal! Son 1.6 por litro!" , (litros*1.6),"€"
if (gasolina==4):
	print "Has elegido SuperPlomo Con Aditivo! Son 1.65 por litro!" , (litros*1.65),"€"
if (gasolina==5):
	print "Has elegido Diesel Normal! Son 1.7 por litro!" , (litros*1.7),"€"
if (gasolina==6):
	print "Has elegido Diesel Fast & Furius! Son 1.75 por litro!" , (litros*1.75),"€"
