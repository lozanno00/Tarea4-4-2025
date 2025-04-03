def determinante(matriz):
    det = 0
    for i in range(len(matriz)):
        submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
        det += ((-1) ** i) * matriz[0][i] * determinante(submatriz)
    return det 

matriz_3x3=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]