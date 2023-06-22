import codecs
from algoritmos.vigenere import cifrar_vigenere, descifrar_vigenere
from algoritmos.cesar import cifrar_cesar, descifrar_cesar
from algoritmos.autoclave import cifrar_autoclave, descifrar_autoclave


def leer_archivo(path):
    with codecs.open(path, 'r', 'utf-8') as file:
        return file.read()


def escribir_archivo(path, contenido):
    with codecs.open(path, 'w', 'utf-8') as file:
        file.write(contenido)


def cifrar_opcion(opcion, texto_plano, clave):
    if opcion == '1':
        desplazamiento = int(input('Desplazamiento: '))
        texto_cifrado = cifrar_cesar(texto_plano, desplazamiento)
        return texto_cifrado

    elif opcion == '2':
        texto_cifrado = cifrar_vigenere(texto_plano, clave)
        return texto_cifrado

    elif opcion == '3':
        texto_cifrado = cifrar_autoclave(texto_plano, clave)
        return texto_cifrado


def descifrar_opcion(opcion, texto_cifrado, clave):
    if opcion == '1':
        desplazamiento = int(input('Desplazamiento: '))
        texto_descifrado = descifrar_cesar(texto_cifrado, desplazamiento)
        return texto_descifrado

    elif opcion == '2':
        texto_descifrado = descifrar_vigenere(texto_cifrado, clave)
        return texto_descifrado

    elif opcion == '3':
        texto_descifrado = descifrar_autoclave(texto_cifrado, clave)
        return texto_descifrado


def main():
    texto_plano = leer_archivo('./files/texto_claro.txt')
    clave = leer_archivo('./files/clave.txt')

    opciones_algoritmo = {
        '1': 'Cesar',
        '2': 'Vignere',
        '3': 'Autoclave'
    }

    opcion = input('Cifrar (1) o Descifrar (2)? ')
    if opcion == '1':
        print('Selecciona un algoritmo:')
        for key, value in opciones_algoritmo.items():
            print(f'{key}. {value}')
        algoritmo = input('Opción: ')
        if algoritmo in opciones_algoritmo.keys():
            texto_cifrado = cifrar_opcion(algoritmo, texto_plano, clave)
            escribir_archivo('./files/texto_cifrado.txt', texto_cifrado)
            print(f'Cifrado {opciones_algoritmo[algoritmo]}: {texto_cifrado}')
        else:
            print('Opción inválida')

    elif opcion == '2':
        print('Selecciona un algoritmo:')
        for key, value in opciones_algoritmo.items():
            print(f'{key}. {value}')
        algoritmo = input('Opción: ')
        if algoritmo in opciones_algoritmo.keys():
            texto_cifrado = leer_archivo('./files/texto_cifrado.txt')
            texto_descifrado = descifrar_opcion(
                algoritmo, texto_cifrado, clave)
            escribir_archivo('./files/texto_descifrado.txt', texto_descifrado)
            print(
                f'Descifrado {opciones_algoritmo[algoritmo]}: {texto_descifrado}')
        else:
            print('Opción inválida')

    else:
        print('Opción inválida')


if __name__ == '__main__':
    main()
