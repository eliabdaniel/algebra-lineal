# Funciones para convertir matrices y fracciones a LaTeX

from fractions import Fraction
from pylatex import Document, Command, NoEscape
from pylatex.package import Package


def fraccion_a_latex(f):
    f = Fraction(f)
    if f.denominator == 1:
        return str(f.numerator)
    signo = '-' if f < 0 else ''
    return f'{signo}\\frac{{{abs(f.numerator)}}}{{{f.denominator}}}'


def matriz_a_latex(M):
    filas = []
    for fila in M:
        elementos = [fraccion_a_latex(x) for x in fila]
        filas.append(' & '.join(elementos))
    cuerpo = ' \\\\ '.join(filas)
    return f'\\begin{{pmatrix}} {cuerpo} \\end{{pmatrix}}'


def nuevo_documento(titulo):
    doc = Document(documentclass='article')
    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('geometry', options='margin=2cm'))
    doc.packages.append(Package('inputenc', options='utf8'))
    doc.packages.append(Package('babel', options='spanish'))

    doc.preamble.append(Command('title', titulo))
    doc.preamble.append(Command('author', 'Eliab'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    return doc
