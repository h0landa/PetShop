from petshop import animal
print('''Digite uma opção abaixo:
1-Para cadastrar Animais;
2-Para Funcionarios;
3-Para Produtos;''')

nomes = []
especies = []
raças = []
nascimento = []

opção = int(input())
if opção == 1:
    for c in range(0,2):
        print('***Cadastro de Animais***')
        print('-' * 25)
        animal.nome = input(str('Digite  o nome do seu Pet: '))
        nomes.append(animal.nome)
        print('-'*25)
        animal.anoNascimento = int(input('Qual o ano de nascimento: '))
        nascimento.append(animal.anoNascimento)
        print('-' * 25)
        animal.raça = input(str('Digite a raça do seu bichinho: '))
        raças.append(animal.raça)
        print('-' * 25)
        animal.especie = input(str('Digite a especia do seu Pet: '))
        especies.append(animal.especie)
        print('-'*25)
        print('    ##Dados do seu Bixinho##    ')
        print(animal.verDados(animal))
        print(f'Idade do animal:{animal.idade(animal)}')

    print('-' * 35 )

    print(f'''
     +++ Dados_Animais +++
    
    Nome dos animais:{nomes}
    Raça dos animais:{raças}
    Especie dos animais:{especies}
              ''')

    print('-' * 35)

from petshop import Funcionario

nomes3 = []
função1 = []

if opção == 2:
    for z in range(0,2):
        print('***Cadastro de Funcionarios***')
        Funcionario.nome = input(str('Digite o nome: '))
        nomes3.append(Funcionario.nome)
        Funcionario.valorPorHora = int(input('Digite o valor por hora: '))
        Funcionario.quantidadeHoras = int(input('Digite a quantidade de horas: '))
        Funcionario.função = input(str('Digite a Função: '))
        função1.append(Funcionario.função)
        print('##Dados_do_Funcionario##')
        print(Funcionario.verDados2(Funcionario))
        print('-' * 30)
        print(f'Salario do Funcionario = R${Funcionario.salario(Funcionario)}')
        print('-' * 30)

    print(f'''
         +++Nome dos Funcionarios e suas Funções+++
        
        Nomes:{nomes3}
        Funções:{função1}''')

from petshop import Produto

if opção == 3:

    marcas = []
    nomes1 = []
    preços = []
    quantidades = []
    total = []

    for x in range(0,2):
        print('***Cadastro de Produtos***')
        print('-' * 25)
        nomes1.append(input(str('Digite o nome do produto: ')))
        print('-' * 25)
        marcas.append(input(str('Digite a marca do produto: ')))
        print('-' * 25)
        Produto.preço = int(input('Digite o preço: '))
        preços.append(Produto.preço)
        print('-' * 25)
        Produto.quantidade = int(input('Digite a quantidade: '))
        quantidades.append(Produto.quantidade)
        print('-' * 25)

        Produto.quantidadeGeral = sum(quantidades)

        print(f'''
        +++Dados_Produtos+++
        Marcas cadastradas:{marcas}
        Preços:{preços}
        Quantidade:{quantidades}
        ''')

    print(f'Valor total em estoque:R${Produto.VTEE(Produto)}')
    print('-' * 25)
















