menu = """
Selecione a ação desejada:

[1] Fazer depósito
[2] Realizar saque
[3] Consultar extrato
[0] Sair do sistema

>> """

# Estado da conta
saldo = 0.0
limite_por_saque = 500.0
historico = []
contador_saques = 0
limite_saques_diario = 3

def efetuar_deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        historico.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito efetuado com sucesso!")
    else:
        print("Erro: valor inválido para depósito.")

def efetuar_saque(valor):
    global saldo, contador_saques
    if valor <= 0:
        print("Erro: valor inválido para saque.")
    elif valor > saldo:
        print("Erro: saldo insuficiente.")
    elif valor > limite_por_saque:
        print(f"Erro: o saque não pode ser maior que R$ {limite_por_saque:.2f}.")
    elif contador_saques >= limite_saques_diario:
        print("Erro: limite diário de saques atingido.")
    else:
        saldo -= valor
        historico.append(f"Saque: R$ {valor:.2f}")
        contador_saques += 1
        print("Saque realizado com sucesso!")

def exibir_extrato():
    print("\n------- EXTRATO BANCÁRIO -------")
    if not historico:
        print("Nenhuma operação realizada.")
    else:
        for registro in historico:
            print(registro)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("-------------------------------")

while True:
    opcao = input(menu)

    if opcao == "1":
        try:
            quantia = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Entrada inválida, informe um número válido.")
            continue
        efetuar_deposito(quantia)

    elif opcao == "2":
        try:
            quantia = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Entrada inválida, informe um número válido.")
            continue
        efetuar_saque(quantia)

    elif opcao == "3":
        exibir_extrato()

    elif opcao == "0":
        print("Sistema finalizado. Obrigado por utilizar nosso banco!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
