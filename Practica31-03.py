def es_primo(n):
   
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeros_primos_a_partir_de(numero):
    """Genera los primeros 10 números primos mayores o iguales al número dado."""
    primos = []
    while len(primos) < 10:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos