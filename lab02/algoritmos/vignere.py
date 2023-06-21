
import re

from .preprocesar import clean_text, ALPHABET


# cifrar con vigenere
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
def descifrar_vigenere(cyphered_text, key, alphabet=ALPHABET):

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
