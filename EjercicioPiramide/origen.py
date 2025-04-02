def torre(n, columna1="1", columna2="2", columna3="3"):
    if n>0:
        torre(n-1, columna1, columna2, columna3)
        print(f"Mueve el disco {n} de la columna {columna1} a la columna {columna3}")
        torre(n-1, columna2, columna1, columna3)

piedras=int(input("Introduce el numero de piedras que usaras:"))
torre(piedras)
