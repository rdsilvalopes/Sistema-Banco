# coding: utf-8

import datetime


class CadastroUsuario:

    # Conta as tentativas de saque e depósito
    tentativa = 0
    # Armazena em Float os depósitos realizados pela Def set_deposito
    hist_depot = []
    # Armazena a data e hora de depósito realizada pela Def set_deposito
    data_depot = []
    # Armazena em Float os Saques feitos pela Def set_saque
    hist_saq = []
    # Armazena a data e hora dos saques feitos pela Def set_saque
    data_saq = []

    def __init__(self, nome, sobrenome, saldo, deposito):
        self._nome = nome
        self.sobrenome = sobrenome
        self.saldo = saldo
        self.deposito = deposito
        self.saque = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        # return self.nome

    def set_deposito(self, deposito):
        now2 = datetime.datetime.today()
        # Add na lista o valor depositado
        dados.hist_depot.append(float(dados.deposito)) # gravar o histórico de depósito para gerar extrato
        # Add na lista a hora do depositado
        dados.data_depot.append(str(now2.strftime('%D %B %Y %H:%M:%S')))
        self.saldo += deposito # grava o saldo
        return self.deposito

    def set_saque(self, saque):
        now1 = datetime.datetime.today()
        # Add na lista o valor sacado
        dados.hist_saq.append(float(dados.saque))
        # Add na lista a hora do saque
        dados.data_saq.append(str(now1.strftime('%D %B %Y %H:%M:%S')))
        self.saldo -= saque
        return self.saque

    @staticmethod
    def extrato_saq():
        # Se nenhum depósito foi realizado, ou seja, tabela vazia []
        if not dados.hist_saq:
            print('R$ 0.00')
        else:
            # Concatena as duas listas com ZIP e imprime os resultados
            for data in zip(dados.data_saq, dados.hist_saq):
                print('{0} \nR${1:.2f}'.format(data[0], data[1]))

    @staticmethod
    def extrato_depot_quinz():
        # Se nenhum depósito foi realizado, ou seja, tabela vazia []
        if not dados.hist_depot:
            print('R$ 0.00')
        else:
            # Concatena as duas listas com ZIP e imprime os resultados
            # [:5] Vai imprimir os 5 primeiros itens da fatia
            for data in zip(dados.data_depot, dados.hist_depot[:    5]):
                print('{0} \nR${1:.2f}'.format(data[0], data[1]))
            print('-----------------------------')
            print('++ CINCO ÚLTIMOS DEPÓSITOS ++')

    @staticmethod
    def extrato_depot_full():
        # Se nenhum depósito foi realizado, ou seja, tabela vazia []
        if not dados.hist_depot:
            print('R$ 0.00')
        else:
            # Concatena as duas listas com ZIP e imprime os resultados
            for a, b in zip(dados.data_depot, dados.hist_depot):
                print('{0} \nR${1:.2f}'.format(a, b))
            print('-----------------------------')
            print('+++++  EXTRATO COMPLETO +++++')

    @staticmethod
    def valida_saque():
        while True:

            # O máximo de tentativas com falha é três...
            #   para operações de saque e depósito.
            if dados.tentativa >= 3:
                print()
                print('--MÁXIMO DE TRÊS TENTATIVAS--')
                print('******* DESCONECTADO ********')
                print('--------- 2233-4455 ---------')
                exit()

            # Tratamento para que não seja utilizado string
            try:
                dados.saque = float(input('Saque:>> '))
            except ValueError:
                print('-----------------------------')
                print('++  OPERAÇÃO NÃO REALIZADA ++')
                print('+++++ Exemplo: R$100.12 +++++')
                dados.tentativa += 1
                continue

            # Não é possível realizar saques de valores negativos
            if dados.saque < 0:
                print('-----------------------------')
                print('++  OPERAÇÃO NÃO REALIZADA ++')
                print('+++++ OPERAÇÃO INVÁLIDA +++++')
                # Quando a operação falha, o contador é incrementado.
                dados.tentativa += 1
                continue

            # Quando o valor sacado é maior que o valor em conta
            if dados.saque > dados.saldo:
                print('-----------------------------')
                print('++  OPERAÇÃO NÃO REALIZADA ++')
                print('Saldo R${0:.2f}'.format(dados.saldo), 'insuficiente')
                dados.tentativa += 1
                break

            # Invoca a função Set_saque e imprime o valor sacado
            if dados.saque <= dados.saldo:
                print('=============================')
                print('-----| SAQUE REALIZADO |-----')
                print('=============================')
                print('>>> R${0:.2f}'.format(dados.set_saque(dados.saque)))
                print()
                # Quando a operação é realizada com sucesso, o contador é zerado.
                dados.tentativa = 0

            break

    @staticmethod
    def valida_deposito():
        while True:

            # O máximo de tentativas é três, para operações de saque e depósito.
            # Quando a operação é realizada com sucesso, o contador é zerado.
            if dados.tentativa >= 3:
                print()
                print('--MÁXIMO DE TRÊS TENTATIVAS--')
                print('******* DESCONECTADO ********')
                print('--------- 2233-4455 ---------')
                exit()

            # Tratamento para que não seja utilizado string
            try:
                dados.deposito = float(input('>>> R$ '))
            except ValueError:
                print('-----------------------------')
                print('++  DEPÓSITO NÃO REALIZADO ++')
                print('+++ Modo correto R$100.12 +++')
                dados.tentativa += 1
                continue

            # Não é possível realizar depósito de valores negativos
            if dados.deposito <= 0:
                print('-----------------------------')
                print('++  OPERAÇÃO NÃO REALIZADA ++')
                print('+++++ DEPÓSITO INVÁLIDO +++++')
                dados.tentativa += 1
                continue
            else:
                print('=============================')
                print('----| DEPÓSITO REALIZADO|----')
                print('=============================')

                # Invoca a função Set_deposito e imprime o valor depositado
                print('>>> R${0:.2f}'.format(dados.set_deposito(dados.deposito)))

                #   Deposito realizado com sucesso, a tentativa que conta erros zera
                dados.tentativa = 0
            break


dados = CadastroUsuario(nome='', sobrenome='', saldo=0, deposito=0)


def main():

    #   Acessa a variavel privada fora da Class
    dados.CadastroUsuario_nome = str.title(input('Nome completo: \n')).split(' ')

    print("\n" * 200)
    while True:
        print()
        print('=============================')

        #   Acessa a variável privada _nome fora da Class..
        # e retorna a primeira string
        print('       Olá,', dados.CadastroUsuario_nome[0])

        print('      |- Bem-vindo(a)-|')
        print('=============================')
        print('-----| Banco do Brasil |-----')
        print('=============================')

        # Se saldo zero, oculta opção S Saque
        # Se saldo Negativo, mostra opção S Saque
        if not dados.saldo:
            print('D - Depósito\n'
                  'C - Consulta Saldo\n'
                  'A - Extrato Saque\n'
                  'Z - Extrato Depósito Quinzenal\n'
                  'P - Extrato Depósito Completo')
            print('=============================')
            op = str(input('>> Opção: '))
        else:
            print('D - Depósito\n'
                  'C - Consulta Saldo\n'
                  'S - Saque\n'
                  'A - Extrato Saque\n'
                  'Z - Extrato Depósito Quinzenal\n'
                  'P - Extrato Depósito Completo')
            print('=============================')
            op = str(input('>> Opção: '))

        # Despósito

        if op == 'd' or op == 'D':
            print()
            print('=============================')
            print('-----| BBB - DEPÓSITO |------')
            print('=============================')
            dados.valida_deposito()     # Invoca a função

        # Consulta saldo

        if op == 'c' or op == 'C':
            print('=============================')
            print('--------| BB - SALDO |--------')
            print('=============================')
            print('Saldo Total R$%.2f' % dados.saldo)     # Mostra o Saldo em conta
            print()

        # Saque

        if op == 's' or op == 'S':
            print()
            print('=============================')
            print('-------| BBB - SAQUE |-------')
            print('=============================')
            dados.valida_saque()     # Invoca a função

        # Extrato Saque

        if op == 'a' or op == 'A':
            print()
            print('=============================')
            print('---| BBB - EXTRATO SAQUE |---')
            print('=============================')
            dados.extrato_saq()     # Invoca a função

        # Extrato Depósito Quinzenal

        if op == 'z' or op == 'Z':
            print()
            print('=============================')
            print('-| BBB - EXTRATO DEPÓSITO |--')
            print('=============================')
            dados.extrato_depot_quinz()     # Invoca a função

        # Extrato Depósito Full

        if op == 'p' or op == 'P':
            print()
            print('=============================')
            print('-| BBB - EXTRATO DEPÓSITO |--')
            print('=============================')
            dados.extrato_depot_full()     # Invoca a função


main()
