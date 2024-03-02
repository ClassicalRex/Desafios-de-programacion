# Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.
import re

palabra_1 = input('Ingrese su 1ra palabra: ')
palabra_2 = input('Ingrese su 2da palabra: ')

def verificador():
    anagrama = True
    lista_palabra_2 = list(palabra_2)
    for i in range(len(palabra_1)):
        if len(palabra_1) == len(palabra_2) and palabra_1[0+i] in lista_palabra_2:
            lista_palabra_2.remove(palabra_1[0+i])
            i+1
        else:
            anagrama = False
            break
    if palabra_1 == palabra_2:
        print('Son la misma palabra')
    elif anagrama:
        print(f'{palabra_1} es un anagrama de {palabra_2}')
    else:
        print(f'{palabra_1} y {palabra_2} no son anagramas')

verificador()