#!/usr/bin/python3.6
#-- coding: utf-8 --
#función:
def es_palindromo(texto):
	respuesta=True
	for i in range(0, len(texto)):
  		if (texto[i] != texto[len(texto)-i-1]):
			respuesta=False
	return(respuesta)

#main
frase='radar'
if (es_palindromo(frase)):
	print( frase + ' es palíndromo')
else:
	print( frase + ' no es palíndromo')
