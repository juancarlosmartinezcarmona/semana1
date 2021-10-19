#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

class Persona(object):
	def  __init__ (self, nombre, edad, dni, telefono,email):
		self.nombre=nombre
		self.edad=edad
		self.dni=dni
		self.telefono=telefono
		self.email=email
	def setNombre (self, nombre):
		self.nombre=nombre
	def setEdad (self, edad):
		self.edad=nombre
	def setDni (self, dni):
		self.dni=dni
	def settelefono (self, telefono):
		self.telefono=telefono
	def setEmail (self, email):
		self.email=email
		
	def getNombre (self):
		return self.nombre
	def getEdad (self):
		return self.edad
	def getDni (self):
		return self.dni
	def getTelefono (self):
		return self.telefono
	def getEmail (self):
		return self.email
		
	def mostrar (self):
		print(self.getNombre())
		print(self.getEdad())
		print(self.getDni())
		print(self.getTelefono())
		print(self.getEmail())
		
	def esMayorDeEdad(self):
		return(self.edad>=18)
		
#main (pruebas):
#creamos la instancia
p1=Persona('Juan', 17, '26852547S','568745654','juan@gmail.com')
#probamos método get
print(p1.getNombre())
#probamos método set
p1.setNombre('Pedro')
print(p1.getNombre())
p1.mostrar()
if (p1.esMayorDeEdad()):
	print('Es mayor de edad', p1.getEdad())
else:
	print ('Es menor de edad', p1.getEdad())
		
	
	
