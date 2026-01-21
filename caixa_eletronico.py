status = True
saldo = 1000.00

while status:
    print("\nCAIXA ELETRÔNICO\n")
    print(" 1 - Verificar Saldo\n",
          "2 - Depositar Dinheiro\n",
          "3 - Sacar Dinheiro\n",
          "4 - Sair")
    opcao = int(input("\nEscolha uma opção (1-4): "))

    if opcao == 1:
        print(f"Saldo Disponível: R${saldo}")
    elif opcao == 2:
        deposito = float(input("Digite o valor do depósito: R$"))
        saldo += deposito
    elif opcao == 3:
        saque = float(input("Digite o valor do saque: R$"))
        saldo -= saque
    elif opcao == 4:
        status = False
        print("Fechando Sistema...")
    else:
        print("Opção Inválida! Tente um número de 1 a 4.")
