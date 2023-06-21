from .preprocesar import clean_text, ALPHABET


def cifrar_cesar(texto_plano, desplazamiento, alfabeto=ALPHABET):
    # se limpia el texto plano
    texto_plano = clean_text(texto_plano)
    # se declara variable texto_cifrado vacia
    texto_cifrado = ''
    # se recorre el texto plano en mayusculas
    for char in texto_plano.upper():
        # si el caracter esta en el alfabeto
        if char in alfabeto:
            # se obtiene el indice del caracter en el alfabeto al cual se le suma el desplazamiento y se obtiene el modulo
            index = (alfabeto.index(char) + desplazamiento) % len(alfabeto)
            # se agrega el caracter cifrado al texto cifrado
            texto_cifrado += alfabeto[index]
            # si no esta en el alfabeto
        else:
            # se agrega el caracter al texto cifrado
            texto_cifrado += char
    return texto_cifrado


def descifrar_cesar(texto_cifrado, desplazamiento, alfabeto=ALPHABET):
    # se limpia el texto cifrado
    texto_cifrado = clean_text(texto_cifrado)
    # se declara variable texto_descifrado vacia
    texto_descifrado = ''
    # se recorre el texto cifrado en mayusculas
    for char in texto_cifrado.upper():
        # si el caracter esta en el alfabeto
        if char in alfabeto:
            # se obtiene el indice del caracter en el alfabeto al cual se le resta el desplazamiento y se obtiene el modulo
            index = (alfabeto.index(char) - desplazamiento) % len(alfabeto)
            # se agrega el caracter descifrado al texto descifrado
            texto_descifrado += alfabeto[index]
            # si no esta en el alfabeto:
        else:
            # se agrega el caracter al texto descifrado
            texto_descifrado += char
        return texto_descifrado
