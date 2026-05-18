# Ejercicio 3: matriz inversa por metodo de la adjunta

import os
import numpy as np
from fractions import Fraction
from pylatex import Section, NoEscape

from utils import fraccion_a_latex, matriz_a_latex, nuevo_documento


def det(M):
    # Determinante por expansion de cofactores en la primera fila
    M = np.array(M, dtype=object)
    n = M.shape[0]
    if n == 1:
        return Fraction(M[0, 0])
    if n == 2:
        return Fraction(M[0,0])*Fraction(M[1,1]) - Fraction(M[0,1])*Fraction(M[1,0])

    total = Fraction(0)
    for j in range(n):
        menor = np.delete(np.delete(M, 0, axis=0), j, axis=1)
        total += ((-1)**j) * Fraction(M[0, j]) * det(menor)
    return total


def cofactores(M):
    M = np.array(M, dtype=object)
    n = M.shape[0]
    C = np.empty((n, n), dtype=object)
    for i in range(n):
        for j in range(n):
            # El menor es eliminar la fila i y la columna j
            menor = np.delete(np.delete(M, i, axis=0), j, axis=1)
            C[i, j] = ((-1)**(i+j)) * det(menor)
    return C


def leer_matriz():
    n = int(input('Tamano (n x n): n = '))
    print('Ingresa los valores fila por fila:')
    M = []
    for i in range(n):
        fila = input(f'Fila {i+1}: ').strip().split()
        M.append([Fraction(v) for v in fila])
    return np.array(M, dtype=object)


def generar_pdf(M, d, C, Adj, Inv, archivo='salidas/03_inversa'):
    doc = nuevo_documento('Matriz Inversa por la Adjunta')

    with doc.create(Section('Matriz original')):
        doc.append(NoEscape(r'\[A = ' + matriz_a_latex(M) + r'\]'))

    with doc.create(Section('Paso 1: Determinante')):
        doc.append(NoEscape(r'\[\det(A) = ' + fraccion_a_latex(d) + r'\]'))
        doc.append(NoEscape(r'Como $\det(A) \neq 0$, la matriz tiene inversa.'))

    with doc.create(Section('Paso 2: Matriz de cofactores')):
        doc.append(NoEscape(
            r'Cada $c_{ij} = (-1)^{i+j} \cdot \det(M_{ij})$, '
            r'donde $M_{ij}$ es el menor (la matriz que queda al eliminar la fila $i$ y la columna $j$).'
        ))
        doc.append(NoEscape(r'\[C = ' + matriz_a_latex(C) + r'\]'))

    with doc.create(Section('Paso 3: Matriz adjunta')):
        doc.append(NoEscape(r'La adjunta es la transpuesta de la matriz de cofactores:'))
        doc.append(NoEscape(r'\[\text{Adj}(A) = C^{T} = ' + matriz_a_latex(Adj) + r'\]'))

    with doc.create(Section('Paso 4: Matriz inversa')):
        doc.append(NoEscape(r'\[A^{-1} = \frac{1}{\det(A)} \cdot \text{Adj}(A)\]'))
        doc.append(NoEscape(r'\[A^{-1} = ' + matriz_a_latex(Inv) + r'\]'))

    doc.generate_tex(archivo)
    print(f'\nArchivo generado: {archivo}.tex')


def main():
    os.makedirs('salidas', exist_ok=True)
    print('Matriz Inversa por la Adjunta')

    op = input('Usar matriz de ejemplo? (s/n): ').strip().lower()
    if op == 's':
        M = np.array([
            [Fraction(1), Fraction(2), Fraction(3)],
            [Fraction(0), Fraction(4), Fraction(5)],
            [Fraction(1), Fraction(0), Fraction(6)]
        ], dtype=object)
    else:
        M = leer_matriz()

    print('Matriz:')
    print(M)

    d = det(M)
    print(f'Determinante = {d}')

    if d == 0:
        print('No tiene inversa.')
        return

    C = cofactores(M)
    print('Cofactores:')
    print(C)

    Adj = C.T
    print('Adjunta:')
    print(Adj)

    n = Adj.shape[0]
    Inv = np.empty((n, n), dtype=object)
    for i in range(n):
        for j in range(n):
            Inv[i, j] = Fraction(Adj[i, j]) / d

    print('Inversa:')
    print(Inv)

    generar_pdf(M, d, C, Adj, Inv)


if __name__ == '__main__':
    main()
