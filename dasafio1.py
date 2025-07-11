# Interface do usuário
menu_opcoes = """
Escolha uma opção:

[1] Depositar
[2] Sacar
[3] Ver Extrato
[0] Sair

>> """

# Variáveis principais
saldo_atual = 0
limite_saque = 500
movimentacoes = []
total_saques = 0
MAX_SAQUES_DIARIOS = 3

# Loop principal
while True:
    escolha = input(menu_opcoes)

    if escolha == "1":
        valor_deposito = float(input("Digite o valor para depósito: "))

        if valor_deposito > 0:
            saldo_atual += valor_deposito
            movimentacoes.append(f"Depósito de R$ {valor_deposito:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido! Tente novamente.")

    elif escolha == "2":
        valor_saque = float(input("Digite o valor para saque: "))

        if valor_saque <= 0:
            print("Valor inválido! Tente novamente.")
        elif valor_saque > saldo_atual:
            print("Saque não autorizado: saldo insuficiente.")
        elif valor_saque > limite_saque:
            print("Saque não autorizado: valor excede o limite permitido por saque.")
        elif total_saques >= MAX_SAQUES_DIARIOS:
            print("Saque não autorizado: número máximo de saques atingido.")
        else:
            saldo_atual -= valor_saque
            movimentacoes.append(f"Saque de R$ {valor_saque:.2f}")
            total_saques += 1
            print("Saque efetuado com sucesso!")

    elif escolha == "3":
        print("\n========= EXTRATO DE MOVIMENTAÇÕES =========")
        if not movimentacoes:
            print("Nenhuma movimentação registrada.")
        else:
            for item in movimentacoes:
                print(item)
        print(f"Saldo atual: R$ {saldo_atual:.2f}")
        print("============================================")

    elif escolha == "0":
        print("Encerrando sistema. Até logo!")
        break

    else:
        print("Opção inválida. Escolha uma das opções do menu.")
