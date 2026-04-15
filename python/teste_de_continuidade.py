num = 0
pare = False
div2 = []
div3 = []
div2_3 = []
num = 0

while not pare:
    num = int(input("Digite um número: "))
    if num % 2 == 0 and num % 3 == 0:
        div2_3.append(num)
        print("Números divisíveis por 2 e por 3.")
        print(div2_3)
    elif num % 2 == 0:
        div2.append(num)
        print("Números divisíveis por 2.")
        print(div2)
    elif num % 3 == 0:
        div3.append(num)
        print("Números divisíveis por 3.")
        print(div3)
    elif num <= 0:
        print("Programa encerrado.")     
        pare = True
    else:
        print("O número não é divisível por 2 nem por 3.")
    