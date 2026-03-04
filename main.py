
mensagem = input("Digite a mensagem! ")
chave = int(input("Digite a chave de deslocamento: "))

print("Mensagem: ", mensagem)
print("Chave: ", chave)

for cadaLetra in mensagem:

    formula = (ord(cadaLetra) - ord('a') + chave) %26 + ord('a')
    nova_letra = chr(formula) 
    print(nova_letra)
