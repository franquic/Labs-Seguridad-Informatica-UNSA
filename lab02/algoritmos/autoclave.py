# importar funciones de preprocesamiento
from .preprocesar import clean_text, ALPHABET

# cifrado por autoclave
def cifrar_autoclave(text, key, alphabet=ALPHABET):
    # se convierte el texto y la clave a mayusculas
    text = text.upper()
    key = key.upper()
    # se limpia el texto y la clave
    text = clean_text(text)
    key = clean_text(key)
    # se declara variable texto_cifrado vacia
    cyphered_text = ''
    # se inicializa el indice en 0
    i = 0
    # se recorre el texto desde el indice 0 hasta el tamaño del texto
    while i < len(text):
        # si el caracter esta en el alfabeto
        if text[i] in alphabet:
            # se obtiene el indice del caracter en el alfabeto al cual se le suma el desplazamiento y se obtiene el modulo
            text_index = alphabet.index(text[i])
            # se obtiene el indice del caracter y se busca [i % len(key)] para que no se salga de rango
            key_index = alphabet.index(key[i % len(key)])

            if i > len(key)-1:
                key_index = alphabet.index(text[(i - len(key)) % len(text)])

            cyphered_text += alphabet[(text_index + key_index) % len(alphabet)]
        else:
            # Si el carácter no está en el alfabeto, se agrega directamente al texto cifrado
            cyphered_text += text[i]

        # Incrementa el índice para avanzar al siguiente carácter del texto
        i += 1

    return cyphered_text

# descifrado con autoclave
def descifrar_autoclave(cyphered_text, key, alphabet=ALPHABET):
    # se convierte el texto cifrado y la clave a mayusculas
    cyphered_text = cyphered_text.upper()
    key = key.upper()

    # se limpia el texto cifrado y la clave
    cyphered_text = clean_text(cyphered_text)
    key = clean_text(key)

    # se declara variable texto vacia
    text = ''
    # se inicializa el indice en 0
    i = 0
    # se recorre el texto cifrado desde el indice 0 hasta el tamaño del texto cifrado
    while i < len(cyphered_text):
        # si el caracter cifrado esta en el alfabeto
        if cyphered_text[i] in alphabet:
            # se obtiene el indice del caracter cifrado en el alfabeto
            text_index = alphabet.index(cyphered_text[i])
            # se obtiene el indice del caracter de la clave y se busca [i % len(key)] para que no se salga de rango
            key_index = alphabet.index(key[i % len(key)])

            if i > len(key)-1:
                # Utiliza caracteres del texto descifrado para generar el índice de la clave
                key_index = alphabet.index(text[(i - len(key))])

            # Calcula el índice resultante restando los índices del texto cifrado y de la clave, y luego tomando
            # el módulo con respecto a la longitud del alfabeto para asegurar que no se salga de rango
            text += alphabet[(text_index - key_index) % len(alphabet)]
        else:
            # Si el carácter cifrado no está en el alfabeto, se agrega directamente al texto descifrado
            text += cyphered_text[i]

        # Incrementa el índice para avanzar al siguiente carácter del texto cifrado
        i += 1

    return text
