import dis
def factorial(n):
    resultado = 1
    for i in range (1, n+1):
        resultado *=1
    return resultado

dis.dis(factorial)