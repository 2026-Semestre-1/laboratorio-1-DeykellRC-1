"""
Nombre: Calculadora
Entradas: Operacion, Num1, Num2
Salidas: resultado de la operacion y numeros que se eligen
Restricciones: no se puede dividir entre 0
                los parametros deben de ser de tipo entero
                los operadores deben de ser de tipo entero
                
"""

def calculadora(operador, num1, num2):
    if not isinstance(operador, int):
        return "Error: el operador debe ser de tipo entero"
    elif not  0 < operador < 5:
        return "Error: el parametro de operador es de 1 a 4"
    elif not isinstance(num1, int):
        return "Error: el valor num1 debe ser de tipo entero"
    elif not isinstance(num2, int):
        return "Error: el valor num2 debe ser de tipo entero"


    
    return calculadora_aux(operador, num1, num2)

def calculadora_aux(operador, num1, num2):

    resultado = 0
    
    if operador == 1:
        return (num1 + num2)

    if operador == 2:
        return (num1 - num2)
 
    if operador == 3:
        return (num1 * num2)

    if operador == 4:
        return (num1 / num2)

"""
Nombre: Contador Digitos
Entradas: num, digito
Salidas: numero de veces que aparece el digito en el numero
Restricciones: Los parametros deben de ser de tipo entero
                Digito debe ser menor a 10 y mayor o igual a 0
"""

def contadorDigitos(num, digito):
    
    if not isinstance(num, int):
        return "Error: el valor de num debe ser entero"
    elif not isinstance(digito, int):
        return "Error: el valor de digito debe ser entero"
    elif (num < 0):
        return "Error: el valor de num debe ser mayor a cero"
    elif (digito <= 0):
        return "Error: el valor de digito debe ser mayor a cero"
    elif (digito >= 10):
        return "Error: el valor de digito debe ser menor a 10"
    return contadorDigitos_aux(num, digito)

def contadorDigitos_aux(num, digito):

    contador = 0

    while (num > 0):
        
        i = num % 10
        
        if (digito == i):
            contador += 1
        num //= 10

    return contador





        

"""
Nombre: Contador_V2
Entradas: inicio, fun, distancia, excepcion
Salidas: suma total de los numeros desde el inicio al final
Restricciones:todos los parametros deben ser de tipo entero
                Los párametros distancia y excepcion debe ser menor a 10 y mayor a 0
                Los valores de inicio y fin deben ser positivos
                Si la distancia es un número negativo, el valor de fin debe ser menor a inicio
                Si la distancia es un número positivo, el valor de fin debe ser mayor a inicio
                Si excepcion es igual a cero, se debe ignorar este valor, lo contrario,
                todo número dentro de la secuencia entre inicio y ** final** sea divisible
                por esta excepcion debe omitirse en la suma
"""


def contador_V2(inicio, fin, distancia, excepcion):
    if not isinstance(inicio, int):
        return "Error: el valor de inicio debe ser entero"
    elif not isinstance(fin, int):
        return "Error: el valor de fin debe ser entero"
    elif not isinstance(distancia, int):
        return "Error: el valor de distancia debe ser entero"
    elif not isinstance(excepcion, int):
        return "Error: el valor de excepcion debe ser entero"
    if (inicio < 0):
        return "Error: el valor de inicio debe ser mayor a cero"
    if (fin < 0):
        return "Error: el valor de fin debe ser mayor a cero"











