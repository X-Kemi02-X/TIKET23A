def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1

def calcularSubtotal(val1,val2,val3):
    subtotalSinDescuento=val1*val2
    subtotal=(subtotalSinDescuento*val3)/100
    total=subtotalSinDescuento-subtotal
    return total

def calcularValorHora(numero1):
    valorhora=numero1/160
    return valorhora

def calcularValorDescuento(val1,val2):
    valordescuento= (val1*val2)/100
    return valordescuento

def consultarMulta(tipo):
    if tipo == 1:
        return 10/100*100
    elif tipo ==2:
        return 15/100*100
    elif tipo == 3:
        return 20/100*100
    elif tipo == 4:
        return 30/100*100
    else:
        return -1
   
 