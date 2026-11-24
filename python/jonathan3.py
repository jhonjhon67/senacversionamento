soma = 0
quantidade = 0
anterior = 0

while True:
    entrada = input("Digite um número positivo (ou 'p' para parar): ")

    if entrada == "p":
        print("Você parou. A sequência é crescente.")
        break

    numero = int(entrada)

    if numero <= 0:
        print("O número deve ser maior que zero!")
        continue

    if numero <= anterior:
        print("A sequência não é crescente. Entrada interrompida.")
        break

    soma += numero
    quantidade += 1
    anterior = numero

print(f"Quantidade de números: {quantidade}")
print(f"Soma: {soma}")