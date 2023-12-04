def nrPrim(nr, div = 2):
    if nr < 2: return 0
    while div < nr:
        if nr % div == 0: return 0
        div += 1
    return 1

def sumaCif (nr, s = 0):
    while nr > 0:
        s += nr % 10
        nr /= 10
    return s

nr = None

while True:
    nr = int(input("nr="))
    if nr < 0:
        break
    cont = 0
    if  nrPrim(sumaCif(nr)) == 1:
        cont += 1

print(cont)
    