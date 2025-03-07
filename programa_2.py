print('Este é o meu segundo programa de cadastramento utilizando Python')
# Iniciando a escrita dos códigos e o testes
print('Por favor, informe os seguintes dados:')

nome = input('Nome: ')
endereco = input('Rua: ')
estado = input('Estado: ')
pais = input('País: ')
telefone = input('Telefone (somente números): ')
email = input('E-mail: ')

idade = input('Idade: ')
while not idade.isdigit():
    print("Por favor, insira uma idade válida (somente números).")
    idade = input('Idade: ')

data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
while len(data_nascimento) != 10 or not data_nascimento[2] == '/' or not data_nascimento[5] == '/':
    print("Por favor, insira uma data válida no formato DD/MM/AAAA.")
    data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')

profissao = input('Profissão: ')
escolaridade = input('Escolaridade (Fundamental, Médio, Superior): ')

continuar = input('Deseja cadastrar outra pessoa? (s/n): ').lower()
while continuar == 's':
    nome = input('Nome: ')
    endereco = input('Rua: ')
    estado = input('Estado: ')
    pais = input('País: ')
    telefone = input('Telefone (somente números): ')
    email = input('E-mail: ')

    idade = input('Idade: ')
    while not idade.isdigit():
        print("Por favor, insira uma idade válida (somente números).")
        idade = input('Idade: ')

    data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
    while len(data_nascimento) != 10 or not data_nascimento[2] == '/' or not data_nascimento[5] == '/':
        print("Por favor, insira uma data válida no formato DD/MM/AAAA.")
        data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')

    profissao = input('Profissão: ')
    escolaridade = input('Escolaridade (Fundamental, Médio, Superior): ')
    
    continuar = input('Deseja cadastrar outra pessoa? (s/n): ').lower()

# Finalizando meu programa.
print('\nCadastro realizado com sucesso! Aqui estão os dados informados:')
print(f'Nome: {nome}')
print(f'Endereço: {endereco}')
print(f'Estado: {estado}')
print(f'País: {pais}')
print(f'Telefone: {telefone}')
print(f'E-mail: {email}')
print(f'Idade: {idade}')
print(f'Data de Nascimento: {data_nascimento}')
print(f'Profissão: {profissao}')
print(f'Escolaridade: {escolaridade}')

# Programa aprovado!