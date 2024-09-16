def titulo(txt, cor='\033[36m'):

    """-> Função Para Titulo e Cor Azul. Retorna uma String
    Param1 - Txt 
    Param2 - Cor (opcional)
    """
    print(f"{cor}{'-' * 30}{txt}{cor}{'-' * 30}{cor}")

def mensagem(msg, cor='\033[36m'):

    """-> Função Para Mensagem. Utilizada como (print)
    Param 1 - msg
    Param 2 - cor 
    """
    print(f"{cor}{msg}{cor}")

def verificar_cpf(cpf: str) -> bool:
    """
    Verifica um CPF (Cadastro de Pessoa Física) número.
    Param 1: cpf (str)
    Returns: boolean True se o CPF for válido, False caso contrário.
    """
    #Função Não Utilizada afim de testes Mais rapidos e para evitar vazamento de dados
    #Pois o video sera postado no publico
    # Remova qualquer caractere não dígito do CPF de entrada
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifique se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcule o primeiro dígito do CPF
    soma1 = sum(int(digito) * peso for digito, peso in zip(cpf, range(10, 1, -1)))
    digito1 = 11 - (soma1 % 11)
    if digito1 > 9:
        digito1 = 0

    # Calcule o segundo dígito do CPF
    soma2 = sum(int(digito) * peso for digito, peso in zip(cpf, range(11, 1, -1)))
    digito2 = 11 - (soma2 % 11)
    if digito2 > 9:
        digito2 = 0

    # Verifique se os dígitos calculados coincidem com os últimos dois dígitos do CPF
    return cpf[-2] == str(digito1) and cpf[-1] == str(digito2)


def menu_usuario():
    """-> Função Para Usuarios sem permissao
    Contem Try, While True.
    Não Tem Parametro
    Retorna para oo Primeiro_menu()
    """
    try:
        while True:
            mensagem("Bem vindo a AutoProblems")
            mensagem("1 - Realizar Reclamação")
            mensagem("2 - Marcar Agendamento")
            mensagem("3 - Sobre Nos")
            mensagem("4 - Sair (Volta ao Menu de Cadastro)")
            escolha = input("Escolha uma Opção: ")
            if escolha == "1":
                problema = input("Digite em Poucas Palavras sua reclamação: ")
                mensagem(f"Reclamação: {problema}")
                mensagem("-" * len(problema))
                mensagem("Reclamação Registrada com Sucesso!")
                mensagem("Conversaremos com o Sr(a) Por E-mail")
                mensagem("-" * len(problema))
            elif escolha == "2":
                mensagem("Marcar Agendamento")
                mensagem("1 - Agendar Consulta | Revisão")
                mensagem("2 - Voltar")
                escolha2 = input("Escolha uma Opção: ")
                if escolha2 == "1":
                    mensagem("----------------------------------")
                    mensagem("Agendamento de Consulta | Revisão")
                    mensagem("----------------------------------")
                    dia = int(input("Digite em Numero o Dia que deseja Agendar: "))
                    mensagem(f"Horas Disponiveis Para dia {dia} \n1- 13:00\n2- 14:30\n3- 18:00")
                    hora = input('Escolha O Melhor Horario: ')
                    if hora == "1":
                        mensagem("--------------------------------")
                        mensagem(f"Agendado para {dia} as 13:00")
                        mensagem("--------------------------------")
                        return menu_usuario()
                    elif hora == "2":
                        mensagem("--------------------------------")
                        mensagem(f"Agendado para {dia} as 14:30")
                        mensagem("--------------------------------")
                        return menu_usuario()
                    elif hora == "3":
                        mensagem("--------------------------------")
                        mensagem(f"Agendado para {dia} as 18:00")
                        mensagem("--------------------------------")
                        return menu_usuario()
                    else:
                        mensagem("-----------------------------")
                        mensagem("      Opção Invalida")
                        mensagem("-----------------------------")
                        return menu_usuario()
                elif escolha2 == "2":
                    mensagem("-----------------------------")
                    mensagem("Voltando ao Menu de Usuário")
                    mensagem("-----------------------------")
                    return menu_usuario()
                else:
                    mensagem("Opção Invalida")
                    return menu_usuario()
            elif escolha == "3":
                mensagem("Sobre Nos")
                mensagem("""
                        -----------------------------------AUTO PROBLEMS----------------------------------------
                        | AutoProblems é uma empresa de serviços de manutenção e reparo para carros            |
                        | com parceria com A PortoSeguro.                                                      |
                        | Tem como Intuito Ajudar os Mecanicos e Usuarios.                                     |
                        | Vendemos peças separadas, realizamos agendamentos para uma Oficina Porto Seguro      |
                        | e muito mais!                                                                        |
                        ----------------------------------------------------------------------------------------""") 
                input("Aperte uma Tecla para voltar ao Menu: ")
                return menu_usuario()
            elif escolha == '4':
                mensagem("---------------------------")
                mensagem("Saindo do Menu de Usuário")
                mensagem("---------------------------")
                return primeiro_menu()
                    
    except:
        mensagem("----------------------")
        mensagem("   Opção Invalida")
        mensagem("----------------------")
        return menu_usuario()
    


def cadastro_do_usuario():
    """-> Função para Cadastro do Usuario (Sem ser ADM)
    Inputs - nome, email, cel, senha, confirma_senha
    E-mail, Nome e Senha Não Podem ser Vazios. 
    senha deve ser igual a confirma senha """
    nome = input("Nome: ")
    email = input("E-mail: ")
    cel = input("Celular: ")
    senha = input("Senha: ")
    confirma_senha = input("Confirme sua Senha: ")
    if not nome or not email or not senha:
        mensagem("-------------------------------------------")
        mensagem("Nome, E-mail e Senha não podem ser vazios.")
        mensagem("-------------------------------------------")
        return cadastro_do_usuario()
    if senha != confirma_senha:
        mensagem("-------------------------------------------")
        mensagem("Senhas não coincidem. Tente novamente.")
        mensagem("-------------------------------------------")
        return cadastro_do_usuario()
    mensagem(f"Seus Dados Estão Corretos?\nNome: {nome}\nE-mail: {email}\nCelular: {cel}")
    verifica_dado = input("1 - Sim\n2 - Nao\nDigite aqui: ")
    if verifica_dado == "1":
        return menu_usuario()
    elif verifica_dado == "2":
        mensagem("-------------------------------------------")
        mensagem("      Refazendo Cadastro. ")
        mensagem("-------------------------------------------")
        return cadastro_do_usuario()
    else:
        mensagem("-------------------------------------------")
        mensagem("      Opção Invalida. Tente novamente.")
        mensagem("-------------------------------------------")
        return cadastro_do_usuario()


def primeiro_menu():
    """-> Função para o Menu Inicial
    Input - Escolha
    Dando a Opção de escolher Se Cadastrar Como Usuario
    Ou Logar como ADM
    """
    titulo("AutoProblems")
    mensagem("1 - Logar como ADM")
    mensagem("2 - Cadastrar como Usuario")
    mensagem("3 - Sair")
    escolha = input("Escolha uma Opção: ")
    if escolha == "1":
        login = input("Digite seu nome: ")
        senha = input("Digite sua Senha: ")
        if login == 'rm556557' and senha == '1234':
            return menu()
        else:
            mensagem("Login ou Senha Incorretos")
            return primeiro_menu()
    elif escolha == "2":
        cadastro_do_usuario()

            

        


def cadastrar_usuario():

    """-> Função Para Cadastrar um Usuario. 
    Inputs: Nome | E-mail | Telefone | Senha | Confirma_Senha
     E-mail Nome e Senhas Não Podem ser Vazios. 
    Se Senha For Diferente de confirma_senha. Volta Pro cadastro 
    Se não - Adiciona inputs ao Dicionario Usuario.
    Retorna Usuario """

    nome = input("Nome: ")
    email = input("E-mail: ")
    cel = input("Celular: ")
    senha = input("Senha: ")
    confirma_senha = input("Confirme sua Senha: ")
    if not nome or not email or not senha:
        mensagem("Nome, E-mail e Senha não podem ser vazios.")
        return cadastrar_usuario()
    if senha != confirma_senha:
        mensagem("Senhas não coincidem. Tente novamente.")
        return cadastrar_usuario()
    mensagem(f"Seus Dados Estão Corretos?\nNome: {nome}\nE-mail: {email}\nCelular: {cel}")
    verifica_dado = input("1 - Sim\n2 - Nao\nDigite aqui: ")
    if verifica_dado == "1":
        usuario = {"nome": nome, "email": email, "cel": cel, "senha": senha}
        return usuario
    elif verifica_dado == "2":
        mensagem("Refazendo Cadastro. ")
        return cadastrar_usuario()
    else:
        mensagem("Opção Invalida. Tente novamente.")
        return cadastrar_usuario()
        

def consultar_usuario(dicionario_usuarios):

    """-> Função Para Consultar Usuario. 
    Param 1 - dicionario_usuarios (Global) 
    Consulta pelo Nome do Usuario.  nome_consulta (Input)
    Para cada Usuario dentro de Diciionario_usuarios. 
    Se Usuario de nome for igual a ao nome_consulta
    Imprime Dados do Usuario
    Se Não - Usuario Não Encontrado """

    nome_consulta = input("Digite o nome do usuário que você deseja consultar: ")
    for chave, usuario in dicionario_usuarios.items():
        if usuario["nome"] == nome_consulta:
            mensagem("------------------------------")
            print("Usuário encontrado!")
            mensagem("------------------------------")
            print(f"Nome: {usuario['nome']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Celular: {usuario['cel']}")
            return
    mensagem("--------------------------------")
    print("Usuário não encontrado. Tente novamente.")
    mensagem("--------------------------------")

def consultar_veiculo(dicionario_veiculo):

    """-> Função Para Consultar Veiculos
    Param 1 - dicionario_veiculo (Global)
    Consulta pela Placa do Veiculo.  placa_consulta (Input)
    Para cada Veiculo dentro de Dicionario_veiculo.
    Se Veiculo de placa for igual a  placa_consulta
    Imprime Dados do Veiculo
    Se Não - Veiculo Não Encontrado 
    """
    placa_consulta = input("Digite a placa do veículo que você deseja consultar: ")
    for chave, veiculo in dicionario_veiculo.items():
        if veiculo["placa"] == placa_consulta:
            mensagem("------------------------------")
            print("Veículo encontrado!")
            mensagem("------------------------------")
            print(f"Marca: {veiculo['marca']}")
            print(f"Modelo: {veiculo['modelo']}")
            print(f"Ano: {veiculo['ano']}")
            print(f"Cor: {veiculo['cor']}")
            return
    mensagem("--------------------------------")   
    print("Veículo não encontrado. Tente novamente.")
    mensagem("--------------------------------")

def listar_usuarios(dicionario_usuarios):
    """-> Função Para Listar Todos os Usuarios
    Param 1 - Dicionario_usuarios (Global)
    Para cada Usuario dentro Dicionario_usuarios
    Imprima Usuario"""

    mensagem("------------------------------")
    for chave, usuario in dicionario_usuarios.items():
        print(f"Nome: {usuario['nome']}")
        print(f"E-mail: {usuario['email']}")
        print(f"Celular: {usuario['cel']}")
        mensagem("------------------------------")

def listar_veiculos(dicionario_veiculo):
    """-> Função Para Listar Todos os Veiculos. 
    Param 1 - Dicionario_veiculo (Global)
    Para cada veiculo dentro de Dicionario_veiculo
    Imprima veiculo 
    """

    mensagem("-------------------------------")
    for chave, veiculo in dicionario_veiculo.items():
        print(f"Marca: {veiculo['marca']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Ano: {veiculo['ano']}")
        print(f"Cor: {veiculo['cor']}")
        print(f"Placa: {veiculo['placa']}")
        mensagem("------------------------------")

def inserir_pecas(estoque):
    """-> Função da Simulaçao de CRUD 
    - > Serve para Inserir Peças de um veiculo 
    Param 1 - Estoque (Global)
    INPUT - nome_peca | codigo | quantidade | Preco | 
    Apos Input adiciona ao dicionario estoque cada Chave com seus respectivos valores """

    nome_peca = input("Digite o nome da peça: ")
    codigo = input("Codigo do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Preço: "))
    estoque.append({"nome": nome_peca, "quantidade": quantidade, 'codigo' : codigo, 'preco' : preco})
    print("Peça inserida com sucesso!")

def alterar_peca(estoque):
    """-> Função Simulaçao CRUD
    -> Serve Para Alterar Peças
    Param 1 - Estoque (Global)
    Input - Nome_peça | quantidade | preco 
    Para cada peça em estoque 
    Se Nome_peca for igual a peça do estoque 
    Altera Quantidade | preco 
    Se Nao - Peca nao encontrada """

    nome_peca = input("Digite o nome da peça que você deseja alterar: ")
    for peca in estoque:
        if peca["nome"] == nome_peca:
            quantidade = int(input("Digite a nova quantidade: "))
            peca["quantidade"] = quantidade
            preco = float(input("Preço: "))
            peca['preco'] = preco
            mensagem("------------------------------")
            print("Peça alterada com sucesso!")
            mensagem("------------------------------")
            return
    mensagem("------------------------------")
    print("Peça não encontrada. Tente novamente.")
    mensagem("------------------------------")

def consulta_pecas(estoque):
    """-> Função Simulação CRUD
    Param 1 - estoque (Global)
    Para cada Peça dentro de estoque 
    Imprima peça
    """

    mensagem("------------------------------")
    for peca in estoque:
        print(f"Nome: {peca['nome']}")
        print(f"Quantidade: {peca['quantidade']}")
        print(f"Codigo: {peca['codigo']}")
        print(f"Preço: {peca['preco']}")
        mensagem("------------------------------")

def excluir_peca(estoque):
    """-> Função para simulação de CRUD
    Serve para excluir uma peça do estoque
    Param 1 - estoque (Global)
    Input - nome_peca 
    Para cada peça dentro de estoque 
    Se nome da peça for igual ao nome_peca
    remove peça
    Se Nao - Peca nao encontrada """

    nome_peca = input("Digite o nome da peça que você deseja excluir: ")
    for peca in estoque:
        if peca["nome"] == nome_peca:
            estoque.remove(peca)
            mensagem("------------------------------")
            print("Peça excluída com sucesso!")
            mensagem("------------------------------")
            return
    mensagem("------------------------------")
    print("Peça não encontrada. Tente novamente.")
    mensagem("------------------------------")

def cadastrar_veiculo():
    """-> Função Para Cadastrar um Veiculo 
    Input - Marca | Modelo | Placa | Ano | Cor
    Marca | Modelo | Ano | Placa - Não Podem ser Vazios
    Adiciona Variaveis ao dicionario veiculos
    Retorna veiculos """

    marca = input("Marca: ")
    modelo = input("Modelo: ")
    placa = input("Placa: ")
    ano = input("Ano: ")
    cor = input("Cor: ")
    if not marca or not modelo or not ano or not placa:
        mensagem("Marca e/ou Modelo e/ou Ano Não Podem ser vazios")
        return cadastrar_veiculo()
    mensagem(f"Os Dados Do Veiculo estão Corretos?\nMarca {marca}\nModelo: {modelo}\nPlaca: {placa}\nAno: {ano}\nCor: {cor}")
    resposta = input("1 - Sim\n2 - Nao\nDigite aqui: ")
    if resposta == '1':
        veiculos = {'marca': marca, 'modelo': modelo, 'ano': ano, 'cor': cor, 'placa': placa}
        return veiculos
    if resposta == '2':
        return cadastrar_veiculo()
    else:
        mensagem("Resposta Invalida")
        return cadastrar_veiculo()

# CODIGO PRINCIPAL
#Variaveis Globais 
dicionario_usuarios = {}
dicionario_veiculo = {}
escolha = 0
estoque = []
adm = {'email': 'rm556557@fiap.com', 'senha': '123'}

#Tente Fazer um While True 
#Com titulo de AutoProblems (Nome Empresa)
#Opções - 1 Cadastrar | 2 Consultar | Listar Todos | Crud Peças | Sair
def menu():
    try:
        while True:
            titulo("Auto Problems")
            mensagem("1. Cadastrar")
            mensagem("2. Consultar")
            mensagem("3. Listar todos")
            mensagem("4. CRUD peças")
            mensagem("5. Sair")

            opcao = input("Digite Aqui: ")

            if opcao == "1":  #Opção Cadastro - Pode Cadastrar um Veiculo ou um Usuario
                print("1. Cadastrar usuário")
                print("2. Cadastrar veículo")
                cadastro_opcao = input("Digite Aqui: ")
                if cadastro_opcao == "1": #Cadastro Usuario 
                    usuario = cadastrar_usuario()
                    dicionario_usuarios[len(dicionario_usuarios)] = usuario
                    mensagem("------------------------------")
                    print("Usuário cadastrado com sucesso!")
                    mensagem("------------------------------")
                elif cadastro_opcao == "2": #Cadastro Veiculo
                    veiculo = cadastrar_veiculo()
                    dicionario_veiculo[len(dicionario_veiculo)] = veiculo
                    mensagem("------------------------------")
                    print("Veiculo cadastrado com sucesso!")
                    mensagem("------------------------------")
                else:
                    mensagem("------------------------------")
                    print("Opção inválida. Tente novamente.")
                    mensagem("------------------------------")

            elif opcao == "2": #Consultar - Pode Consultar um Veiculo ou Um Carro
                print("1. Consultar usuário")
                print("2. Consultar veículo")
                consulta_opcao = input("Digite Aqui: ")
                if consulta_opcao == "1": #Consulta Usuario
                    consultar_usuario(dicionario_usuarios)
                elif consulta_opcao == "2": #Consulta Veiculo 
                    consultar_veiculo(dicionario_veiculo)
                else:
                    mensagem("------------------------------")
                    print("Opção inválida. Tente novamente.")
                    mensagem("------------------------------")

            elif opcao == "3": #Listar Todos - Pode Listar Todos os Usuarios e Todos os Veiculos 
                print("1. Listar todos os usuários") 
                print("2. Listar todos os veículos")
                lista_opcao = input("Digite Aqui: ")
                if lista_opcao == "1": #Lista Todos os Usuarios 
                    mensagem("------------------------------")
                    listar_usuarios(dicionario_usuarios)
                elif lista_opcao == "2": #Lista Todos os Veiculos 
                    mensagem("------------------------------")
                    listar_veiculos(dicionario_veiculo)
                else:
                    mensagem("------------------------------")
                    print("Opção inválida. Tente novamente.")
                    mensagem("------------------------------")

            elif opcao == "4": #Crud Peças - Podendo Inserir | Alterar | Consultar | Excluir | Voltar ao Menu
                escolha = 0
                while escolha != 5:
                    print("1 - Inserir Peças")
                    print("2 - Alterar Peças")
                    print("3 - Consultar Peças")
                    print("4 - Excluir Peças")
                    print("5 - Voltar ao menu principal")

                    escolha = int(input("Digite Aqui: "))

                    if escolha == 1: #Insere Peças
                        inserir_pecas(estoque)
                    elif escolha == 2: #Altera peças 
                        alterar_peca(estoque)
                    elif escolha == 3: #Consulta Peças
                        consulta_pecas(estoque)
                    elif escolha == 4: #Exclui Peças 
                        excluir_peca(estoque)
                    elif escolha == 5: #Volta ao Menu Principal 
                        mensagem("------------------------------")
                        print("Voltando ao menu principal...")
                        mensagem("------------------------------")
                    else:
                        mensagem("------------------------------")
                        print("Opção inválida. Tente novamente.")
                        mensagem("------------------------------")

            elif opcao == "5": #Finaliza O Programa
                mensagem("------------------------------")
                print("Encerrando  o Sistema...")
                mensagem("------------------------------")
                break

            else: 
                mensagem("------------------------------")
                print("Opção inválida. Tente novamente.")
                mensagem("------------------------------")

    except Exception as e:
        print(f"Erro: {e}")

primeiro_menu()