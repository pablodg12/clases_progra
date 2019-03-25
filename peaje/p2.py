def calcular_precio(llegada):
    precio_total = 0
    for letra_2 in llegada:
        if letra_2 == 'M':
            precio_total = precio_total + 1000
        elif letra_2 == 'C':
            precio_total += 5000
        elif letra_2 == 'A':
            precio_total += 2500
    return(precio_total)
