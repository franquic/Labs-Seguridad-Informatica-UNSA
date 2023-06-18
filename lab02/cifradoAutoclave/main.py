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
    return text

# eliminar signos de puntuacion y esapcios en blanco
def clean_text(text):
    text = remove_tildes(text)
    text = re.sub(r'[\s\W]+', '', text)
    return text


ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# cifrado por autoclave
def cifrado_autoclave(text, key, alphabet=ALPHABET):
    text = text.upper()
    key = key.upper()
    
    text = clean_text(text)
    key = clean_text(key)
    

    cyphered_text = ''
    i = 0
    while i < len(text):
        if text[i] in alphabet:
            text_index = alphabet.index(text[i])
            key_index = alphabet.index(key[i % len(key)])

            if i > len(key)-1:
                key_index = alphabet.index(text[(i - len(key)) % len(text)])

            cyphered_text += alphabet[(text_index + key_index) % len(alphabet)]
            
        else:
            cyphered_text += text[i]

        i += 1

    return cyphered_text


# descifrado con autoclave
def descifrado_autoclave(cyphered_text, key, alphabet=ALPHABET):
    cyphered_text = cyphered_text.upper()
    key = key.upper()
    
    cyphered_text = clean_text(cyphered_text)
    key = clean_text(key)
    

    text = ''
    i = 0
    while i < len(cyphered_text):
        if cyphered_text[i] in alphabet:
            text_index = alphabet.index(cyphered_text[i])
            key_index = alphabet.index(key[i % len(key)])

            if i > len(key)-1:
                key_index = alphabet.index(text[(i - len(key))])

            text += alphabet[(text_index - key_index) % len(alphabet)]
            
        else:
            text += cyphered_text[i]

        i += 1

    return text



    
if __name__ == '__main__':
    text = 'autoclave'
    key = 'LUNA'
    cyphered_text = cifrado_autoclave(text, key)
    print(cyphered_text)
    print(descifrado_autoclave(cyphered_text, key))

    