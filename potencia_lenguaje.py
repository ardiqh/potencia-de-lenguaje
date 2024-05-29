import itertools

def potencia_lenguaje(tamano_alfabeto, alfabeto, longitud_maxima):
    palabras = []
    for longitud in range(1, longitud_maxima + 1):
        combinaciones = itertools.product(alfabeto, repeat=longitud)
        palabras.extend([''.join(palabra) for palabra in combinaciones])
    return palabras

def main():
    tamano_alfabeto = int(input("Ingrese el tamaño del alfabeto: "))
    alfabeto = []
    for i in range(tamano_alfabeto):
        letra = input(f"Ingrese el elemento {i+1} del alfabeto: ")
        alfabeto.append(letra)
    longitud_maxima = int(input("Ingrese la longitud máxima de las palabras: "))

    resultado = potencia_lenguaje(tamano_alfabeto, alfabeto, longitud_maxima)
    print("El lenguaje generado es:")
    print(resultado)

if __name__ == "__main__":
    main()