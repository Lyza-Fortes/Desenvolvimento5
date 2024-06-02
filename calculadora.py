def calculadora():
    while True: 
        print("\nEscolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        escolha = int(input("Digite o número da operação desejada: ")) 
        if escolha == 0:
            print("Saindo...")
            break
        elif escolha <= 4: 
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            if escolha == 1:
                resultado = num1 + num2
                print(f"Resultado da Soma: {resultado}")
            elif escolha == 2:
                resultado = num1 - num2
                print(f"Resultado da Subtração: {resultado}")
            elif escolha == 3:
                resultado = num1 * num2
                print(f"Resultado da Multiplicação: {resultado}")
            elif escolha == 4:
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f"Resultado da Divisão: {resultado}")
        else:
            print("Essa opção não existe. Por favor, escolha uma opção válida.")

calculadora()