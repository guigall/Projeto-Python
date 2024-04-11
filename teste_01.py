# criando um sistema bancário
# Saque 
# Deposito
# Visualizar Extrato


menu = """

[1] SACAR
[2] DEPOSITO
[3] EXTRATO
[4] SAIR

-> """

saldo = 0
limite = 500
exatrato = ""
numero_saques = 0
LIMITE_DE_SAQUES = 3

while  True:

    opcao = input(menu)

    if opcao == "1":
        valor_de_saque = float(input("Qual o valor desejado para sacar: \n"))

        exedeu_saques = numero_saques >= LIMITE_DE_SAQUES

        if exedeu_saques:
            print("Limite de saques atigindo")
            break

        elif valor_de_saque > saldo:
            print("Valor desejado acima do disponivel")
        
        elif valor_de_saque > limite:
            print("Valor desejado acima do limite permitido\n")

        elif valor_de_saque <= 0:
            print("Valor impossivel de ser sacado")

        elif valor_de_saque < saldo:
            saldo -= valor_de_saque
            exatrato += f"\nvalor sacado: ${valor_de_saque:.2f} \n"
            numero_saques += 1

            
    elif opcao == "2":
        valor_de_deposito = float(input("Informe o valor desejado para deposito:  "))

        if valor_de_deposito <= 0:
            print("Operação impossivel de ser realizada")
            
        elif valor_de_deposito > 0:
            saldo += valor_de_deposito
            exatrato += f"Deposito de ${valor_de_deposito:.2f}"


    elif opcao == "3":
        print(" **************************** \n")
        print("Não foram realizados movimentações" if not exatrato else exatrato)
        print(f"\n SALDO: ${saldo:2.2f}")
        print(" \n**************************** ")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, Por gentileza informe novamente a operação que deseja")



