#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

#Adivina el número. Genera un número aleatorio del 1 al 100. el usuario debe 
#adivinarlo con un máximo número de intentos que él mismo introduce.
from random import randint
resultado=False;
numero=randint(1,100)
print("Introduzca número de intentos:")
maxi=int(input())
intento=1
while ((intento<=maxi) and (not resultado)):
	print("Le quedan ", maxi-intento+1 ," intentos: ")
	intento+=1
	entrada=int(input())
	if (entrada<numero):
		print ("El número es mayor que ", entrada)
	elif (entrada>numero):
		print ("El número es menor que " , entrada)
	else:
		resultado=True
		break
if (resultado):
	print ("Lo has conseguido!!!")
else:
	print ("El número era ", numero, ". Fin del juego, suerte la próxima vez")
	

