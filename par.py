# Conta até 100_000_000_000 e separa os números pares em uma lista

pares = []
for i in range(1, 10001):
    if i % 2 == 0:
        pares.append(i)

print(pares)

# Atenção: esse código consome muita memória e tempo!
# Para testar, use um valor -- muito menor, como 10_000.