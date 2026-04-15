cont = 0

print("Sistema de verificação de divisibilidade")

num_min = int(input("Digite um número mínimo: "))
num_max = int(input("Digite um número máximo: "))

print(f"Números divisíveis por 5 entre {num_min} e {num_max}:")

if num_min > num_max:
    print("O número mínimo deve ser menor ou igual ao número máximo.")
else:
    for num in range(num_min, num_max + 1):
        if num % 5 == 0:
            print(num)
            cont += 1
    print(f"Total de números divisíveis por 5 é {cont}")
