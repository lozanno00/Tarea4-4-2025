def eliminar_termino(polinomio, grado):
    
    if grado < len(polinomio):
        polinomio[-(grado + 1)] = 0  # Elimina el término estableciendo su coeficiente en 0
    return polinomio

polinomio = [1, 2, 3, 4]  # Representación del polinomio: 1x^3 + 2x^2 + 3x + 4
grado = 1
resultado = eliminar_termino(polinomio, grado)
print(resultado)

