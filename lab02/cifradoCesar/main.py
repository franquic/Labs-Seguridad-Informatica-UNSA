# Importamos el módulo argparse para manejar los argumentos de línea de comandos
import argparse

# Definimos la clase CifradoCesar
class CifradoCesar:
    # El método __init__ se llama cuando creamos una nueva instancia de la clase
    def __init__(self, desplazamiento):
        # Guardamos el desplazamiento que se usará para el cifrado. Este valor se pasa cuando se crea una nueva instancia de la clase.
        self.desplazamiento = desplazamiento
        # Definimos el alfabeto que se usará para el cifrado
        self.alfabeto = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # Calculamos el módulo, que es la longitud del alfabeto
        self.mod = 27

    # Método para cifrar un texto plano
    def cifrar(self, texto_plano):
        # Inicializamos el texto cifrado como una cadena vacía
        texto_cifrado = ''
        # Iteramos sobre cada carácter en el texto plano
        for char in texto_plano.upper():
            # Si el carácter está en nuestro alfabeto
            if char in self.alfabeto:
                # Calculamos el índice del carácter cifrado
                indice = (self.alfabeto.index(char) + self.desplazamiento) % self.mod
                # Agregamos el carácter cifrado al texto cifrado
                texto_cifrado += self.alfabeto[indice]
            else:
                # Si el carácter no está en nuestro alfabeto, lo dejamos sin cambios
                texto_cifrado += char
        # Devolvemos el texto cifrado
        return texto_cifrado

    # Método estático para leer un texto plano desde un archivo y cifrarlo
    @staticmethod
    @staticmethod
    def desde_archivo(ruta_archivo, desplazamiento):
        # Abrimos el archivo en modo lectura, especificando la codificación
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            # Leemos el contenido del archivo
            texto_plano = archivo.read()
        # Ciframos el contenido del archivo y lo devolvemos
        return CifradoCesar(desplazamiento).cifrar(texto_plano)


# Este bloque se ejecuta si el script se ejecuta directamente (en lugar de importarse como un módulo)
if __name__ == "__main__":
    # Creamos un analizador de argumentos
    parser = argparse.ArgumentParser(description='Caesar Cipher')
    # Agregamos los argumentos que aceptará nuestro script
    parser.add_argument('-f', '--file', help='Direccion del archivo a cifrar')
    parser.add_argument('-t', '--text', help='Texto plano a cifrar')
    parser.add_argument('-s', '--shift', type=int, help='Desplazamiento para el cifrado')
    # Parseamos los argumentos de la línea de comandos
    args = parser.parse_args()

    # Si se proporcionó un archivo, leemos el texto del archivo y lo ciframos
    if args.file:
        print(CifradoCesar.desde_archivo(args.file, args.shift))
    # Si se proporcionó un texto, lo ciframos
    elif args.text:
        print(CifradoCesar(args.shift).cifrar(args.text))
    # Si no se proporcionó ni un archivo ni un texto, mostramos un mensaje de error
    else:
        print("Por favor proporcione un archivo o un texto")
