qut = int(input("Digite a quantidade de valores que você deseja verificar: "))
l = []
temp = 0

for i in  range(qut):    
    nmr = int(input(f"Digite o {i + 1} número: "))
    if nmr <= 0:
        print("Número inválido. Por favor, digite um número positivo.")
        continue
    else:
        l.append(nmr)

for i in  range(len(l)):
    for n in range(i + 1, len(l)):
        if l[i] > l[n]:
            temp = l[i]
            l[i] = l[n]
            l[n] = temp

print(l)        