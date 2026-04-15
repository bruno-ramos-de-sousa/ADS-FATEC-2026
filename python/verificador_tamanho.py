qut = int(input("Digite a quantidade de valores que você deseja verificar: "))
l = []
temp = 0

for i in  range(qut):    
    nmr = int(input(f"Digite o {i + 1} número: "))
    l.append(nmr)

for i in  range(qut):
    for n in range(i + 1, qut):
        if l[i] > l[n]:
            temp = l[i]
            l[i] = l[n]
            l[n] = temp

print(l)        