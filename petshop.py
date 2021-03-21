class animal:


    def __init__(self,nome,raça,anoNascimento,especie):
        self.nome = nome
        self.raça = raça
        self.anoNascimento = anoNascimento
        self.especie = especie

    def idade(self):

        return 2021 - animal.anoNascimento

    def verDados(self):
        return f'''
        Nome: {animal.nome}
        Especie:{animal.especie}
        Raça:{animal.raça}
        Ano de nascimento:{animal.anoNascimento}
                '''

#if __name__ == '__main__':
#   a = animal()

#    animais = []

#    animais.append(a.nome)
#   print(animais)



class Produto:
    def __init__(self,marca,nome,preço,quantidade,quantidadeGeral):
        self.nome = quantidadeGeral
        self.nome = nome
        self.marca = marca
        self.preço = preço
        self.quantidade = quantidade


    def VTEE(self):
         #(Valor total em estoque)

        return Produto.preço * Produto.quantidadeGeral


    def verDados1(self):
        return f'O valor total em estoque: R${Produto.VTEE}'


class Funcionario:
    def __init__(self,nome,função,valorPorHora,quantidadeHoras):
        self.quantidadeHoras = quantidadeHoras
        self.valorPorHora = valorPorHora
        self.nome = nome
        self.função = função


    def salario(self):

        return Funcionario.quantidadeHoras * Funcionario.valorPorHora

        #return f'Salario do Funcionario: {montante}'


    def verDados2(self):

        return f'''
        Nome: {Funcionario.nome}
        Quantidades de Horas de serviço: {Funcionario.quantidadeHoras}
        Função: {Funcionario.função}
        Valor por hora: {Funcionario.valorPorHora}'''



