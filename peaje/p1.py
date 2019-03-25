import random
def simular_llegada():
    #n: cantidad de v que llegaran en un intervalo de tiempo
    n = random.randint(0,100)
    llegada = ''
    for i in range(0,n):
        aleatorio = random.randint(0,2)
        if aleatorio == 0:
            llegada += 'M'
        elif aleatorio == 1:
            llegada += 'C'
        elif aleatorio == 2:
            llegada += 'A'        
    return(llegada)
