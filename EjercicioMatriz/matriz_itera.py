def determinante(matriz):
    if len(matriz)!= 3 or len(matriz[0]!= 3):
        print("La matriz debe ser 3x3")

    a,b,c=matriz[0]
    d,e,f=matriz[1]
    g,h,i=matriz[2]


matriz= [
    [1,2,3],
    [3,4,5],
    [6,7,8]
]

resultado=determinante(matriz)
print(resultado)