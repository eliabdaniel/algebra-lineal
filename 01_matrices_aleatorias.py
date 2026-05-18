# Ejercicio 1: matrices aleatorias de varios tipos

import os
import numpy as np
from pylatex import Section, NoEscape

from utils import matriz_a_latex, nuevo_documento


def fila(n=4):
    return np.random.randint(1, 10, size=(1, n))

def columna(n=4):
    return np.random.randint(1, 10, size=(n, 1))

def cuadrada(n=3):
    return np.random.randint(1, 10, size=(n, n))

def rectangular(filas=3, cols=4):
    if filas == cols:
        cols += 1
    return np.random.randint(1, 10, size=(filas, cols))

def diagonal(n=3):
    return np.diag(np.random.randint(1, 10, size=n))

def triangular_superior(n=3):
    return np.triu(np.random.randint(1, 10, size=(n, n)))

def triangular_inferior(n=3):
    return np.tril(np.random.randint(1, 10, size=(n, n)))

def identidad(n=3):
    return np.eye(n, dtype=int)

def nula(filas=3, cols=3):
    return np.zeros((filas, cols), dtype=int)


tipos = {
    '1': ('Fila', fila),
    '2': ('Columna', columna),
    '3': ('Cuadrada', cuadrada),
    '4': ('Rectangular', rectangular),
    '5': ('Diagonal', diagonal),
    '6': ('Triangular Superior', triangular_superior),
    '7': ('Triangular Inferior', triangular_inferior),
    '8': ('Identidad', identidad),
    '9': ('Nula', nula),
}


def menu():
    print('\nTipos de matriz:')
    for k, (nombre, _) in tipos.items():
        print(f'  {k}. {nombre}')
    print('  0. Todas')


def generar_pdf(matrices, archivo='salidas/01_matrices'):
    doc = nuevo_documento('Matrices Aleatorias')
    doc.append(NoEscape('Documento generado con Python y PyLaTeX.'))
    doc.append(NoEscape(r'\\[1em]'))

    for nombre, M in matrices:
        with doc.create(Section(f'Matriz {nombre}')):
            f, c = M.shape
            doc.append(NoEscape(f'Dimension: ${f} \\times {c}$'))
            doc.append(NoEscape(r'\\[0.5em]'))
            doc.append(NoEscape(r'\[A = ' + matriz_a_latex(M) + r'\]'))

    doc.generate_tex(archivo)
    print(f'Archivo generado: {archivo}.tex')


def main():
    os.makedirs('salidas', exist_ok=True)
    menu()
    op = input('\nElige una opcion: ').strip()

    matrices = []
    if op == '0':
        for nombre, f in tipos.values():
            M = f()
            matrices.append((nombre, M))
            print(f'\n{nombre}:')
            print(M)
    elif op in tipos:
        nombre, f = tipos[op]
        M = f()
        matrices.append((nombre, M))
        print(f'\n{nombre}:')
        print(M)
    else:
        print('Opcion invalida, genero una cuadrada')
        matrices.append(('Cuadrada', cuadrada()))

    generar_pdf(matrices)


if __name__ == '__main__':
    main()
