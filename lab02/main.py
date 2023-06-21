from algoritmos.vignere import cifrar_vigenere, descifrar_vigenere
from algoritmos.cesar import cifrar_cesar, descifrar_cesar
from algoritmos.autoclave import cifrar_autoclave, descifrar_autoclave


def main():
    with open('./files/texto_claro.txt', 'r') as f:
        texto_plano = f.read()

    path_texto_cifrado = './files/texto_cifrado.txt'
    path_clave = './files/clave.txt'
    path_texto_descifrado = './files/texto_descifrado.txt'

    opcion = input('Cifrar (1) o Descifrar (2)? ')
    if opcion == '1':
        algoritmo = input('Cesar (1) | Vignere (2) | Autoclave (3)? ')
        if algoritmo == '1':
            desplazamiento = input('Desplazamiento: ')
            texto_cifrado = cifrar_cesar(texto_plano, desplazamiento)
            with open(path_texto_cifrado, 'w') as f:
                f.write(texto_cifrado)
            print(texto_cifrado)

        elif algoritmo == '2':
            with open(path_clave, 'r') as f:
                clave = f.read()
            texto_cifrado = cifrar_vigenere(texto_plano, clave)
            with open(path_texto_cifrado, 'w') as f:
                f.write(texto_cifrado)
            print('Cifrado Vignere: ' + texto_cifrado)

        elif algoritmo == '3':
            with open(path_clave, 'r') as f:
                clave = f.read()
            texto_cifrado = cifrar_autoclave(texto_plano, clave)
            with open(path_texto_cifrado, 'w') as f:
                f.write(texto_cifrado)
            print('Cifrado Autoclave: ' + texto_cifrado)

    elif opcion == '2':
        algoritmo = input('Cesar (1) | Vignere (2) | Autoclave (3)? ')
        if algoritmo == '1':
            desplazamiento = input('Desplazamiento: ')
            with open(path_texto_cifrado, 'r') as f:
                texto_cifrado = f.read()
            texto_descifrado = descifrar_cesar(texto_cifrado, desplazamiento)
            with open(path_texto_descifrado, 'w') as f:
                f.write(texto_descifrado)
            print('Descifrado Cesar: ' + texto_descifrado)

        elif algoritmo == '2':
            with open(path_clave, 'r') as f:
                clave = f.read()
            with open(path_texto_cifrado, 'r') as f:
                texto_cifrado = f.read()
            texto_descifrado = descifrar_vigenere(texto_cifrado, clave)
            with open(path_texto_descifrado, 'w') as f:
                f.write(texto_descifrado)
            print('Descifrado Vignere: ' + texto_descifrado)

        elif algoritmo == '3':
            with open(path_clave, 'r') as f:
                clave = f.read()
            with open(path_texto_cifrado, 'r') as f:
                texto_cifrado = f.read()
            texto_descifrado = descifrar_autoclave(texto_cifrado, clave)
            with open(path_texto_descifrado, 'w') as f:
                f.write(texto_descifrado)
            print('Descifrado Autoclave: ' + texto_descifrado)


if __name__ == '__main__':
    main()
