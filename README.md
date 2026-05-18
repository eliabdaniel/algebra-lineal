# Algebra Lineal con PyLaTeX

Tarea de la materia de Algebra Lineal 2026-I, UFPS.

Son tres ejercicios en Python que usan la biblioteca PyLaTeX para generar documentos en LaTeX con el procedimiento paso a paso:

1. Generar matrices aleatorias de varios tipos (fila, columna, cuadrada, rectangular, diagonal, triangulares, identidad, nula).
2. Calcular el determinante por el metodo de Gauss.
3. Calcular la matriz inversa por el metodo de la adjunta.

## Instalacion

```
pip install -r requirements.txt
```

## Como ejecutar

Cada ejercicio se corre por separado:

```
python 01_matrices_aleatorias.py
python 02_determinante_gauss.py
python 03_matriz_inversa.py
```

Los scripts generan un archivo `.tex` en la carpeta `salidas/`.



## Archivos

- `utils.py` - funciones que se usan en los tres ejercicios
- `01_matrices_aleatorias.py` - ejercicio 1
- `02_determinante_gauss.py` - ejercicio 2
- `03_matriz_inversa.py` - ejercicio 3
- `salidas/` - archivos .tex que generan los scripts

## Lo que aprendi

- PyLaTeX permite generar el codigo LaTeX desde Python, lo cual es comodo porque no toca escribirlo a mano.
- Para que los resultados queden exactos uso fracciones en lugar de decimales. Si uso decimales se acumulan errores de redondeo.
- En el metodo de Gauss el determinante es el producto de la diagonal de la matriz triangular, pero cada vez que intercambio dos filas el signo cambia.
- El metodo de la adjunta para la inversa funciona bien para matrices pequenas, pero si la matriz es grande es muy lento (porque calcular cada cofactor implica otro determinante).

