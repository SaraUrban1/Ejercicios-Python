def decimal(n):
    n = list(n)
    n.reverse()
    decimalito = 0

    for i in range (len(n)):
        decimalito = int(n[i])*2**i
    return decimalito

print (decimal("10110"))

def pasar_binario (n):
    binario = []
    while n > 0:
        binario.append(str(n%2))
        n//=2
    return ''.join(binario)

print (pasar_binario(18))