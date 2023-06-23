def menu():
    menu = '''\n
    =============== MENU ===============
    [D]  Depositar
    [S]  Sacar
    [E]  Extrato
    [NC] Nova Conta
    [L]  Listar Contas
    [NU] Novo Usuário
    [Q]  Sair
    '''
    
    print(menu)

    return input().lower()

def depositar(saldo, valor_deposito, extrato, /):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depositado R${valor_deposito}\n"
    else:
        print("Valor inválido")

    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, numero_saque, limite_saques):
    
    if numero_saque < limite_saques:

        if (valor_saque > limite) or (valor_saque <= 0) or (saldo < valor_saque):
            print("Valor inválido de saque")
        else:
            saldo -= valor_saque
            numero_saque += 1
            extrato += f"Valor sacado R${valor_saque}\n"

    elif numero_saque >= limite_saques:
        print("Limite de saques diários atingidos")

    return saldo, extrato, numero_saque

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário ocom esse CPF!")
        return
    
    nome = input("Inform o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, n° - bairro - cidade/uf): ")
    
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta Criada com Sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("Usuário não encontrato")

def listar_contas(contas):
    for conta in contas:
        linha = f'''
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            '''
        print(linha)

def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saque = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "d":
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor_saque = float(input("Digite o valor a ser sacado, máximo de R$500,00: "))
            saldo, extrato, numero_saque = sacar(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=limite, numero_saque=numero_saque, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":    
            print("Extrato:")
            print(extrato)
            print(f'Saldo atual R${saldo}\n')
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("Selecione uma opção válida!")

main()
