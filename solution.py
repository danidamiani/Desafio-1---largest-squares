import math
import numpy as np

def solution(area):
    rq = int(math.sqrt(area))
    valores = []
    for i in range(1,rq+1):
        valores.append(np.power(i,2))
    resultado = []
    while area>0:
        maior = -1
        for i in range(len(valores)):
            if (valores[i]>maior and valores[i]<=area):
                maior = valores[i]
        resultado.append(maior)
        area = area - maior
    return resultado

