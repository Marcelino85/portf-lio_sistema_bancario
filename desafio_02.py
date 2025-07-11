# Sistema Bancário Modularizado

# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Variáveis fixas
AGENCIA_PADRAO = "0001"
limite_saque = 500
MAX_SAQUES_DIARIOS = 3

# Função Depósito: argumentos posicionais apenas (positional only)
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito de R$ {valor:.2f}")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

# Função Saque: argumentos somente por nome (keyword only)
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Valor inválido para saque.")
    elif valor > saldo:
        print("Saldo insuficiente para saque.")
    elif valor > limite:
        print("Valor do saque excede o limite permitido.")
    elif numero_saques >= limite_saques:
        print("Limite diário de saques atingido.")
    else:
        saldo -= valor
        extrato.append(f"Saque de R$ {valor:.2f}")
        numero_saques += 1
    return saldo, extrato, numero_saques

# Função Extrato: argumentos mistos positional only e keyword only
def extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===================")

# Função para cadastrar usuário
def cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se CPF já existe
    for usuario in usuarios:
        if usuario["cpf"] == cpf_numeros:
            print("Erro: CPF já cadastrado.")
            return usuarios
    
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_numeros,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuarios

# Função para cadastrar conta corrente
def criar_conta(contas, usuarios, cpf):
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    usuario = None
    
    for u in usuarios:
        if u["cpf"] == cpf_numeros:
            usuario = u
            break
    
    if usuario is None:
        print("Usuário não encontrado. Cadastre o usuário antes de criar a conta.")
        return contas
    
    numero_conta = len(contas) + 1
    conta = {
        "agencia": AGENCIA_PADRAO,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    return contas

# Função para listar contas (opcional)
def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        usu = conta["usuario"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usu['nome']} (CPF: {usu['cpf']})")

# Variáveis da conta padrão para operações bancárias
saldo_atual = 0
extrato_movimentacoes = []
numero_saques_hoje = 0

# Menu principal
menu_opcoes = """
Escolha uma opção:

[1] Depositar
[2] Sacar
[3] Ver Extrato
[4] Cadastrar Usuário
[5] Criar Conta Corrente
[6] Listar Contas
[0] Sair

>> """

while True:
    escolha = input(menu_opcoes)

    if escolha == "1":
        try:
            valor = float(input("Informe o valor para depósito: "))
        except ValueError:
            print("Valor inválido, tente novamente.")
            continue
        
        saldo_atual, extrato_movimentacoes = deposito(saldo_atual, valor, extrato_movimentacoes)

    elif escolha == "2":
        try:
            valor = float(input("Informe o valor para saque: "))
        except ValueError:
            print("Valor inválido, tente novamente.")
            continue
        
        saldo_atual, extrato_movimentacoes, numero_saques_hoje = saque(
            saldo=saldo_atual,
            valor=valor,
            extrato=extrato_movimentacoes,
            limite=limite_saque,
            numero_saques=numero_saques_hoje,
            limite_saques=MAX_SAQUES_DIARIOS
        )

    elif escolha == "3":
        extrato(saldo_atual, extrato=extrato_movimentacoes)

    elif escolha == "4":
        nome = input("Nome completo: ").strip()
        nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        cpf = input("CPF (somente números ou com pontuação): ").strip()
        endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ").strip()
        usuarios = cadastrar_usuario(usuarios, nome, nascimento, cpf, endereco)

    elif escolha == "5":
        cpf_busca = input("Informe o CPF do titular da conta: ").strip()
        contas = criar_conta(contas, usuarios, cpf_busca)

    elif escolha == "6":
        listar_contas(contas)

    elif escolha == "0":
        print("Encerrando sistema. Obrigado por usar nosso banco!")
        break

    else:
        print("Opção inválida. Tente novamente.")
