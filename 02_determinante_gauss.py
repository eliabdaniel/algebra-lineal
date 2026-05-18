# Ejercicio 2: determinante por metodo de Gauss

import os
import numpy as np
from fractions import Fraction
from pylatex import Section, NoEscape

from utils import fraccion_a_latex, matriz_a_latex, nuevo_documento


def leer_matriz():
    n = int(input('Tamano (n x n): n = '))
    print(f'Ingresa los valores fila por fila, separados por espacios:')
    M = []
    for i in range(n):
        fila = input(f'Fila {i+1}: ').strip().split()
        M.append([Fraction(v) for v in fila])
    return np.array(M, dtype=object)


def gauss(M):
    A = M.copy()
    n = A.shape[0]
    pasos = [('Matriz inicial:', A.copy())]
    signo = 1

    for i in range(n):
        # Si el pivote es cero, busco otra fila para intercambiar
        if A[i, i] == 0:
            cambio = False
            for k in range(i+1, n):
                if A[k, i] != 0:
                    A[[i, k]] = A[[k, i]]
                    signo *= -1
                    pasos.append((f'Intercambio $F_{{{i+1}}}$ con $F_{{{k+1}}}$ (cambia el signo):', A.copy()))
                    cambio = True
                    break
            if not cambio:
                pasos.append(('No hay pivote, el determinante es 0.', A.copy()))
                return Fraction(0), pasos

        # Hacer ceros debajo del pivote
        for j in range(i+1, n):
            if A[j, i] != 0:
                factor = Fraction(A[j, i]) / Fraction(A[i, i])
                nueva = []
                for c in range(n):
                    nueva.append(Fraction(A[j, c]) - factor * Fraction(A[i, c]))
                A[j] = nueva
                pasos.append((
                    f'$F_{{{j+1}}} \\to F_{{{j+1}}} - ({fraccion_a_latex(factor)})F_{{{i+1}}}$:',
                    A.copy()
                ))

    # El determinante es el producto de la diagonal por el signo acumulado
    det = Fraction(signo)
    for i in range(n):
        det *= Fraction(A[i, i])

    pasos.append((
        f'Matriz triangular superior. Determinante = producto de diagonal $\\times$ ({signo:+d}):',
        A.copy()
    ))
    return det, pasos


def generar_pdf(det, pasos, archivo='salidas/02_determinante'):
    doc = nuevo_documento('Determinante por Metodo de Gauss')

    with doc.create(Section('Procedimiento')):
        for desc, M in pasos:
            doc.append(NoEscape(desc))
            doc.append(NoEscape(r'\[' + matriz_a_latex(M) + r'\]'))

    with doc.create(Section('Resultado')):
        doc.append(NoEscape(r'\[\det(A) = ' + fraccion_a_latex(det) + r'\]'))

    doc.generate_tex(archivo)
    print(f'\nArchivo generado: {archivo}.tex')


def main():
    os.makedirs('salidas', exist_ok=True)
    print('Determinante por Gauss')

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

    det, pasos = gauss(M)
    print(f'\nDeterminante = {det}')

    generar_pdf(det, pasos)


if __name__ == '__main__':
    main()
