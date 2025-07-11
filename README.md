# Sistema Bancário Modularizado em Python

## Descrição

Este sistema bancário simula operações básicas como depósito, saque e consulta de extrato, organizado de forma modular utilizando funções. Além das operações tradicionais, o sistema permite cadastrar usuários e criar contas correntes vinculadas aos usuários cadastrados.

---

## Funcionalidades

### Operações Bancárias

- **Depósito**  
  Função que recebe argumentos posicionais para adicionar um valor ao saldo, registrando a movimentação no extrato.

- **Saque**  
  Função que recebe argumentos apenas por nome (keyword-only) para realizar o saque respeitando limites de saldo, limite por saque e número máximo de saques diários.

- **Extrato**  
  Função que recebe argumentos mistos (positional-only e keyword-only) e exibe todas as movimentações registradas e o saldo atual.

### Cadastro de Usuários e Contas

- **Cadastrar Usuário**  
  Permite registrar um novo usuário com nome, data de nascimento, CPF (armazenado apenas números) e endereço. Impede cadastro duplicado baseado no CPF.

- **Criar Conta Corrente**  
  Cria uma conta vinculada a um usuário existente, identificando-o pelo CPF. O número da conta é sequencial e a agência é fixa ("0001"). Um usuário pode ter múltiplas contas.

- **Listar Contas**  
  Exibe todas as contas cadastradas com seus respectivos titulares.

---

## Detalhes Técnicos

- Uso de listas para armazenar usuários e contas.
- Validação de CPF para evitar duplicidade.
- Controle do limite de saques e valor máximo por saque.
- Modularização com funções específicas que seguem regras distintas para passagem de parâmetros:
  - `deposito`: argumentos posicionais (positional-only)
  - `saque`: argumentos somente por nome (keyword-only)
  - `extrato`: mistura de positional-only e keyword-only
- Interface de texto simples para interação com o usuário.

---

## Como usar

1. Execute o script Python.
2. Utilize o menu para escolher opções como depósito, saque, visualizar extrato, cadastrar usuário, criar conta e listar contas.
3. Para criar conta, primeiro é necessário cadastrar um usuário com CPF válido.
4. Depósitos e saques alteram o saldo da conta padrão para demonstração.
5. O extrato apresenta todas as movimentações realizadas durante a execução.

---

## Exemplo do Menu
Escolha uma opção:

1. Depositar
2. Sacar
3. Ver Extrato
4. Cadastrar Usuário
5. Criar Conta Corrente
6. Listar Contas
0. Sair
