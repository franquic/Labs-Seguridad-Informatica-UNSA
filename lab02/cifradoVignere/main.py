
import re
# eliminar tildes
def remove_tildes(text):
    tildes_dict = {
        'á': 'a', 
        'é': 'e', 
        'í': 'i', 
        'ó': 'o', 
        'ú': 'u', 
        'Á': 'A', 
        'É': 'E', 
        'Í': 'I', 
        'Ó': 'O', 
        'Ú': 'U'
    }

    for k, v in tildes_dict.items():
        text = text.replace(k, v)

    print(text)
    return text

# eliminar signos de puntuacion y esapcios en blanco
def clean_text(text):
    text = remove_tildes(text)
    text = re.sub(r'[\s\W]+', '', text)
    return text


ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
# cifrar con vigenere
# módulo alfabeto módulo 27
def cifrar_vigenere(text, key, alphabet=ALPHABET):
    text = text.upper()
    key = key.upper()
    text = clean_text(text)
    key = clean_text(key)
    

    cyphered_text = ''

    i = 0
    while i < len(text):
        if text[i] in alphabet:
            index_text = alphabet.index(text[i])
            index_key = alphabet.index(key[i % len(key)])
            cyphered_text += alphabet[(index_text + index_key) % len(alphabet)]
        else:
            cyphered_text += text[i]
        
        i += 1

    return cyphered_text

# decifrar con vigenere
def decifrar_vigenere(cyphered_text, key, alphabet=ALPHABET):

    
    key = key.upper()
    cyphered_text = cyphered_text.upper()
    
    text = ''
    i = 0
    while i < len(cyphered_text):
        if cyphered_text[i] in alphabet:
            index_cyphered_text = alphabet.index(cyphered_text[i])
            index_key = alphabet.index(key[i % len(key)])
            text += alphabet[(index_cyphered_text - index_key) % len(alphabet)]
        else:
            text += cyphered_text[i]
        
        i += 1
    
    return text


if __name__ == '__main__':
    with open('texto_claro.txt', 'r') as file:
        text = file.read()
        
    with open('clave.txt', 'r') as file:
        key = file.read()

    with open('texto_cifrado.txt', 'w') as file:
        file.write(cifrar_vigenere(text, key))

    with open('texto_cifrado.txt', 'r') as file:
        cyphered_text = file.read()

    with open('texto_decifrado.txt', 'w') as file:
        file.write(decifrar_vigenere(cyphered_text, key))
        

    

