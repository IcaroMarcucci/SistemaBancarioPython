saldo = 0.0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3

menu = """
[D] - Depositar
[S] - Sacar
[E] - Extrato
[Q] - Sair

-> """

def Deposito():

    global saldo
    global extrato

    valor_deposito = float(input("Digite o valor a ser depositado: "))

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depositado R${valor_deposito}\n"
    else:
        print("Valor inválido")

def Sacar():

    global saldo
    global numero_saque
    global extrato

    if numero_saque < LIMITE_SAQUES:
        valor_saque = float(input("Digite o valor a ser sacado, máximo de R$500,00: "))

        if (valor_saque > 500) or (valor_saque <= 0) or (saldo < valor_saque):
            print("Valor inválido de saque")
        else:
            saldo -= valor_saque
            numero_saque += 1
            extrato += f"Valor sacado R${valor_saque}\n"
    else:
        print("Limite de saques diários atingidos")

while True:
    opcao = input(menu).lower()
    
    if opcao =="d":
        print("Depósito")
        Deposito()
    
    elif opcao =="s":
        print("Saque")
        Sacar()

    elif opcao =="e":    
        print("Extrato:")
        print(extrato)
        print(f'Saldo atual R${saldo}\n')
    
    elif opcao =="q":
        break
    
    else:
        print("Selecione uma opção válida!")
