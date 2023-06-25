from .preprocesar import clean_text, ALPHABET


# cifrado por autoclave
def cifrar_autoclave(text, key, alphabet=ALPHABET):
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
def descifrar_autoclave(cyphered_text, key, alphabet=ALPHABET):
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
