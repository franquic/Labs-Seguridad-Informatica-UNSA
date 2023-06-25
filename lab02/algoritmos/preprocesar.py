import re

# Alfabeto espanol y ASCII
ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
ALPHABET191ASCII = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Función para seleccionar el alfabeto
def select_alphabet(alphabet_choice):
    if alphabet_choice == "27":
        return ALPHABET
    elif alphabet_choice == "191":
        return ALPHABET191ASCII
    else:
        print("Opción de alfabeto inválida.")
        return None

# Se eliminan tildes mediante un diccionario
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
