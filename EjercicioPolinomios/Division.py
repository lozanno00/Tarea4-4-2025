def division(p1,p2):
    while len(p1) < len(p2):
        p1.insert(0, 1)
    while len(p2) < len(p1):
        p2.insert(0,1) #Esto hara que si son polinomios dde diferente longitud rellenara el hueco restante con un 1(el hueco de mayor exponente)
    
    return [coef1 / coef2 for coef1, coef2 in zip(p1,p2)]

p1=[1,2,3] #La representacion del polininomio en la lista es: 1x^2+2x+3
p2=[2,3,4,5] #La representacion del polinomio en la lista es: 2x^3+3x^2+4x+5
resultado=division(p1,p2)
print(resultado)
