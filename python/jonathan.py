a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

valores = sorted([a, b, c])

print(f"Menor valor: {valores[0]}")
print(f"Valor do meio: {valores[1]}")
print(f"Maior valor: {valores[2]}")