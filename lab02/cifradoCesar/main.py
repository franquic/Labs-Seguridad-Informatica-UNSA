import argparse
import re

class CifradoCesar:
    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento
        self.alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        self.mod = len(self.alfabeto)
    # se remueven las tildes, haciendo uso de un diccionario
    def remove_tildes(self, texto):
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
            texto = texto.replace(k, v)
        return texto

    def clean_text(self, texto):
        # se remueven las tildes
        texto = self.remove_tildes(texto)
        # se remueven los signos de puntuacion y espacios en blanco
        texto = re.sub(r'[\s\W]+', '', texto)
        return texto

    def cifrar(self, texto_plano):
        # se limpia el texto plano
        texto_plano = self.clean_text(texto_plano)
        # se declara variable texto_cifrado vacia
        texto_cifrado = ''
        # se recorre el texto plano en mayusculas
        for char in texto_plano.upper():
            # si el caracter esta en el alfabeto
            if char in self.alfabeto:
                # se obtiene el indice del caracter en el alfabeto al cual se le suma el desplazamiento y se obtiene el modulo
                index = (self.alfabeto.index(char) + self.desplazamiento) % self.mod
                # se agrega el caracter cifrado al texto cifrado
                texto_cifrado += self.alfabeto[index]
            # si no esta en el alfabeto
            else:
                # se agrega el caracter al texto cifrado
                texto_cifrado += char
        return texto_cifrado

    def descifrar(self, texto_cifrado):
        # se declara variable texto_descifrado vacia
        texto_descifrado = ''
        # se recorre el texto cifrado en mayusculas
        for char in texto_cifrado.upper():
            # si el caracter esta en el alfabeto
            if char in self.alfabeto:
                # se obtiene el indice del caracter en el alfabeto al cual se le resta el desplazamiento y se obtiene el modulo
                index = (self.alfabeto.index(char) - self.desplazamiento) % self.mod
                # se agrega el caracter descifrado al texto descifrado
                texto_descifrado += self.alfabeto[index]
            # si no esta en el alfabeto 
            else:
                # se agrega el caracter al texto descifrado
                texto_descifrado += char
        return texto_descifrado

    @staticmethod
    def from_file(ruta_archivo, desplazamiento):
        # Abrimos el archivo en modo lectura, especificando la codificación
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            # Leemos el contenido del archivo
            texto_plano = archivo.read()
            #print texto_plano con mensaje texto plano es
            print("Texto plano: ", texto_plano)
        # Ciframos el contenido del archivo y lo devolvemos
        return CifradoCesar(desplazamiento).cifrar(texto_plano)

if __name__ == "__main__":
    # se crea un objeto de tipo ArgumentParser para poder obtener los argumentos de la linea de comandos
    parser = argparse.ArgumentParser(description='Cifrado Cesar')
    # se agregan los argumentos que se van a utilizar, en este caso, file, text y shift; se incluye una ayuda para cada argumento
    parser.add_argument('-f', '--file', help='Ruta al archivo que contiene el texto plano')
    parser.add_argument('-t', '--text', help='El texto plano a ser cifrado')
    parser.add_argument('-s', '--shift', type=int, help='El desplazamiento para el Cifrado Cesar')
    args = parser.parse_args()
    # si es un archivo lo que se va a cifrar entonces se ejecuta el metodo from_file
    if args.file:
        cifrador = CifradoCesar.from_file(args.file, args.shift)
    # si es un texto lo que se va a cifrar de frente se ejecuta el metodo cifrar
    elif args.text:
        cifrador = CifradoCesar(args.shift).cifrar(args.text)
    # si no se proporciona un archivo o un texto para ser cifrado, se muestra el mensaje de error
    else:
        print("Por favor, proporciona un archivo o un texto para ser cifrado.")
        exit()
    # se muestra el texto cifrado y el texto descifrado
    print("Texto cifrado: ", cifrador)
    print("Texto descifrado: ", CifradoCesar(args.shift).descifrar(cifrador))