print('Este é o meu programa de cadastramento utilizando Python')

# Estes são meus primeiros testes
# Este é meu primeiro programa
print('Por favor, informe os seguintes dados:')

nome = input('Nome: ')
endereco = input('Rua: ')
estado = input('Estado: ')
pais = input('País: ')
idade = input('Idade: ')

while not idade.isdigit():
    print("Por favor, insira uma idade válida (somente números).")
    idade = input('Idade: ')

print('\nCadastro realizado com sucesso! Aqui estão os dados informados:')
print(f'Nome: {nome}')
print(f'Endereço: {endereco}')
print(f'Estado: {estado}')
print(f'País: {pais}')
print(f'Idade: {idade}')

# Programa aprovado!