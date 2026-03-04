
mensagem = input("Digite a mensagem! ")
chave = int(input("Digite a chave de deslocamento: "))

print("Mensagem: ", mensagem)
print("Chave: ", chave)

for cadaLetra in mensagem:
    numero = ord(cadaLetra)
    numero = numero + chave
    nova_letra = chr(numero)
    print(nova_letra)
