class Conta:

    def __init__(self, conta, nome, saldo = 0):
        self.cod_conta = conta
        self.nome = nome.upper()
        self.saldo = saldo
    
    def __str__(self):
        return f'Conta nº: {self.cod_conta} - Correntista: {self.nome} - Saldo: {self.saldo}\n'

    def alterar_nome(self):
        self.nome = Erro.testa_nome()
        self.menu()

    def depositar(self):
        msg = 'Digite o valor que deseja depositar: '
        valor = Erro.teste_valor(msg)

        self.saldo += valor
        print('Depósito realizado com sucesso!\n')
        self.menu()

    def sacar(self):
        msg = 'Digite o valor que deseja sacar: '
        valor = Erro.teste_valor(msg)

        if(self.saldo < valor):
            print('Saldo indisponível!\n')
        else:
            self.saldo -= valor
            print('Saque realizado com sucesso!\n')
        self.menu()

    def transferir(self):
        msg = 'Digite o valor que deseja transferir: '
        valor = Erro.teste_valor(msg)

        if (self.saldo < valor):
            print('Saldo indisponível!\n')
            self.menu()

        msg_input = 'Digite o número da conta para qual deseja transferir o valor: '
        msg_err = 'Conta inválida!\n'
        numero = Erro.teste_numero(msg_input, msg_err)

        self.saldo -= valor
        conta = banco.procura_conta(numero)
        conta.saldo += valor
        print('Transferência realizada com sucesso!\n')

        self.menu()

    def menu(self):
        Mensagens.msg_sistema(3)
        resposta = Erro.teste_opcao(1, 7)
        if(resposta == 1):
            self.alterar_nome()
        elif(resposta == 2):
            self.sacar()
        elif(resposta == 3):
            self.depositar()
        elif(resposta == 4):
            self.transferir()
        elif(resposta == 5):
            print(self)
            self.menu()
        elif(resposta == 6):
            banco.tela_inicial()

class Banco:
    lista_de_contas = []

    def tela_inicial(self):
        Mensagens.msg_sistema(2)
        resposta = Erro.teste_opcao(1, 4)
        if(resposta == 1):
            self.criar_conta()
        elif(resposta == 2):
            self.acessa_conta()
        elif(resposta == 3):
            self.exclui_conta()
        elif(resposta == 4):
            exit()

    def criar_conta(self):
        existente = 0

        while existente == 0:
            conta = int(input('Digite o número da conta: '))
            for codigo in self.lista_de_contas:
                if(conta == codigo.cod_conta):
                    existente = 1
            if(existente == 1):
                print('Número de conta já existe!\n')
                existente = 0
            else:
                nome = Erro.testa_nome()
                break

        nova_conta = Conta(conta, nome)
        self.lista_de_contas.append(nova_conta)
        print('Conta criada com sucesso!\n')
        self.tela_inicial()

    def acessa_conta(self):
        msg_input = 'Digite o número da conta: '
        msg_err = 'Conta inválida!\n'
        cod_conta = Erro.teste_numero(msg_input, msg_err)
        conta = self.procura_conta(cod_conta)
        conta.menu()

    def exclui_conta(self):
        msg_input = 'Digite o número da conta que deseja cancelar: '
        msg_err = 'Conta inválida!\n'
        numero = Erro.teste_numero(msg_input, msg_err)
        conta = self.procura_conta(numero)
        print(f'Tem certeza que deseja cancelar a conta de nº: {conta.cod_conta} do cliente: {conta.nome}\n')
        resposta = input('Digite (s) para sim ou (n) para não: ')

        if(resposta.upper() == 'S'):
            if(conta.saldo > 0):
                print('Não é possível excluir a conta, pois a mesma possui saldo positivo!')
                self.tela_inicial()
            if (conta.saldo < 0):
                print('Não é possível excluir a conta, pois a mesma possui saldo negativo!')
                self.tela_inicial()
            else:
                self.lista_de_contas.remove(conta)
                print('Conta excluída com sucesso!\n')
                self.tela_inicial()
        elif(resposta.upper() == 'N'):
            print('Conta mantida!\n')
            self.tela_inicial()
        else:
            print('Opção inválida!\n')
            self.tela_inicial()


    def procura_conta(self, cod_conta):
        for conta in self.lista_de_contas:
            if(cod_conta == conta.cod_conta):
                return conta

        print('Conta não localizada!\n')
        self.tela_inicial()

class Mensagens:

    @staticmethod
    def msg_sistema(escolha):
        if (escolha == 1):
            print('###################################')
            print('### Bem-Vindo ao Banco Tabajara ###')
            print('###################################')
            print('#### Escolha a opção desejada! ####\n')

        elif (escolha == 2):
            print('Escolha  a opção desejada:\n')
            print('1 - Criar uma nova conta')
            print('2 - Acessar uma conta')
            print('3 - Cancelar uma conta')
            print('4 - Sair do Banco')

        elif (escolha == 3):
            print('Escolha a opção desejada:\n')
            print('1 - Alterar o nome do titular da conta')
            print('2 - Realizar saque')
            print('3 - Realizar depósito')
            print('4 - Realizar transferência')
            print('5 - Extrato da conta')
            print('6 - Voltar ao menu anterior')

class Erro:

    @staticmethod
    def teste_valor(msg):
        while True:
            try:
                numero = float(input(msg))
                if (numero <= 0):
                    print('Valor inválido')
                else:
                    break
            except ValueError:
                print('Valor inválido')
        return numero

    @staticmethod
    def teste_numero(msg_input, msg_err):
        while True:
            try:
                numero = int(input(msg_input))
                if (numero <= 0):
                    print(msg_err)
                else:
                    break
            except ValueError:
                print(msg_err)
        return numero

    @staticmethod
    def teste_opcao(valor_inicial, valor_final):
        while True:
            try:
                resposta = int(input("Digite a opção desejada: "))
                if (resposta < valor_inicial or resposta > valor_final):
                    print('Opção digitada inválida!\n')
                else:
                    break
            except ValueError:
                print('Opção digitada inválida!\n')
        return resposta

    @staticmethod
    def testa_nome():
        while True:
            try:
                erro = False
                nome = input('Digite o novo nome do titular: ')
                for i in nome:
                    if i.isdigit():
                        print('Nome inválido!\n')
                        erro = True
                        break
                if(erro):
                    continue
                if(nome == "" or nome == " "):
                    print('Nome inválido!\n')
                else:
                    float(nome)
                    print('Nome inválido!\n')
            except ValueError:
                break
        return nome

banco = Banco()
Mensagens.msg_sistema(1)
banco.tela_inicial()