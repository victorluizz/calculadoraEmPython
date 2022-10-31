# Calculadora em Python
print("\n******************* Python Calculator *******************")

def soma (num1, num2):
    return num1 + num2;

def divisao(num1, num2):
    return num1 / num2;

def mult(num1, num2):
    return num1 * num2;

def sub(num1, num2):
    return num1 - num2;

continua = True

while continua:
    print ("Selecione o número da operação desejada:")
    print("1 - Soma \n2- Subtração \n3- Multiplicação \n4- Divisão")
    escolha = int(input("Digite a sua opção: "))

    escolha_certa = True

    while escolha_certa:

        if (escolha != 1) and (escolha != 2) and (escolha != 3) and (escolha != 4):
            print("Opção inválida!")
            escolha_certa = False
        else:
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))

            if (escolha == 1):
                print("\n")
                print(numero1, "+", numero2, soma(numero1, numero2), "\n")
            elif (escolha == 2):
                print("\n")
                print(numero1, "-", numero2, sub(numero1, numero2), "\n")
            elif (escolha == 3):
                print("\n")
                print(numero1, "*", numero2, mult(numero1, numero2), "\n")
            elif (escolha == 4):
                print("\n")
                print(numero1, "/", numero2, divisao(numero1, numero2), "\n")

        
            reiniciar = input("Deseja realizar outra operação? ")
        
            if (reiniciar == "Não") or (reiniciar == "Nao"):
                print("Calculadora encerrada!")
                continua = False
                escolha_certa = False
    
