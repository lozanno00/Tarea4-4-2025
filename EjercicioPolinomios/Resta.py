def Resta(polinomio1, polinomio2):
    while len(polinomio1) < len(polinomio2):
        polinomio1.insert(0, 0)
    while len(polinomio2) < len(polinomio1):
        polinomio2.insert(0, 0)  #Esto hara que si no son polinomios del mismo tamaño rellenara la posicion vacia con un 0 (el hueco de mayor exponente)

    return [coef1 - coef2 for coef1, coef2 in zip(polinomio1, polinomio2)]

polinomio1=[1,3,4] #La representacion del polinomio en la lista es: 1x^2+3x+4
polinomio2=[2,6] #La representacion del polinomio en la lista es: 2x+6

resultado=Resta(polinomio1,polinomio2)
print(resultado)
