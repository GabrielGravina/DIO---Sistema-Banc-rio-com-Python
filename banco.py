menu = """
Insira a operação
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1500
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao.lower() == "s":
        valor = float(input("Informe o valor do saque: "))


        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao.lower() == "e":
        if not extrato:
            extrato_content = """
================ EXTRATO ================
Não foram realizadas movimentações.
Saldo: R$ {:.2f}
==========================================
            """.format(saldo)
        else:
            extrato_content = """
================ EXTRATO ================
{}
Saldo: R$ {:.2f}
==========================================
""".format(extrato, saldo)

        print(extrato_content.upper())
        
    elif opcao.lower() == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")