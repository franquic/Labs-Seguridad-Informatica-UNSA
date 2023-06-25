# Importar la librería re para utilizar expresiones regulares
import re
# Importar todas las funciones de preprocesar.py
from .preprocesar import *
# cifrar con vigenere
def cifrar_vigenere(text, key, alphabet_choice):
    # Seleccionar el alfabeto
    alphabet = select_alphabet(alphabet_choice)
    # Si el alfabeto es inválido, retornar None
    if alphabet is None: 
        return None
    text = text.upper()  # Convertir el texto a mayúsculas
    key = key.upper()    # Convertir la clave a mayúsculas
    text = clean_text(text)  # Limpiar el texto de caracteres no deseados
    key = clean_text(key)    # Limpiar la clave de caracteres no deseados

    cyphered_text = ''  # Inicializar el texto cifrado
    i = 0
    # Recorrer el texto de acuerdo a la longitud del texto cifrado
    while i < len(text):
        # si el caracter esta en el alfabeto
        if text[i] in alphabet:
            # Obtener el índice del carácter actual en el texto
            index_text = alphabet.index(text[i])
             # Obtener el índice del carácter actual en la clave (repetir la clave si es más corta que el texto)               
            index_key = alphabet.index(key[i % len(key)])
             # Aplicar el cifrado de Vigenère y agregar el carácter cifrado al texto cifrado     
            cyphered_text += alphabet[(index_text + index_key) % len(alphabet)] 
        else:
            # Si el carácter no está en el alfabeto, se agrega al texto cifrado sin cifrar
            cyphered_text += text[i]  
        # se incrementa el contador
        i += 1
    # retornar el texto cifrado
    return cyphered_text

# decifrar con vigenere
def descifrar_vigenere(cyphered_text, key, alphabet_choice):
    # Seleccionar el alfabeto
    alphabet = select_alphabet(alphabet_choice)
    # Si el alfabeto es inválido, retornar None
    if alphabet is None:
        return None
    # Convertir la clave a mayúsculas
    key = key.upper()         
    # Convertir el texto cifrado a mayúsculas       
    cyphered_text = cyphered_text.upper()  
     # Inicializar el texto descifrado
    text = '' 
    # Inicar el contador en 0
    i = 0
    # Recorrer el texto cifrado de acuerdo a la longitud del texto cifrado
    while i < len(cyphered_text):
        # si el caracter esta en el alfabeto
        if cyphered_text[i] in alphabet:
            # Obtener el índice del carácter cifrado actual en el texto cifrado
            index_cyphered_text = alphabet.index(cyphered_text[i])  
             # Obtener el índice del carácter actual en la clave (repetir la clave si es más corta que el texto cifrado)
            index_key = alphabet.index(key[i % len(key)])           
            # Aplicar el descifrado de Vigenère y agregar el carácter descifrado al texto descifrado
            text += alphabet[(index_cyphered_text - index_key) % len(alphabet)]  
        else:
            # Si el carácter no está en el alfabeto, se agrega al texto descifrado sin descifrar
            text += cyphered_text[i]  
        # se incrementa el contador    
        i += 1
    # retornar el texto descifrado
    return text
