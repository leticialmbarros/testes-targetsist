# solicita ao usuário que digite uma string
string = input("Digite uma string: ")

# variável para armazenar a string invertida
string_invertida = ""

# percorre a string de trás para frente e adiciona cada caractere à variável string_invertida
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# imprime a string invertida
print("String invertida: ", string_invertida)
