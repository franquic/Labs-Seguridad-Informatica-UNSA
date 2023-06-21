import re

# Alfabeto espanol
ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'


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
