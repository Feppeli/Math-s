print('Teatcher Math')

#Diálogo inicial
print('''########################
## Qual é o seu nome? ##
########################''')
nome = input()

print(f'Seja bem vindo(a): {nome}')


def calculate():
    print('''############################
##Operações disponíveis:  ##
##                        ##
##1- Soma                 ##
##2- subtração            ##
##3- Divisão              ##
##4- Multiplicação        ##
############################''')


    #seleção do tipo de operação
    operação = int(input('Digite o número da operação que você deseja:'))

    1 == 'soma'
    2 == 'subtração'
    3 == 'divisão'
    4 == 'multiplicação'

    # Operação de Soma
    if operação < int(2): 
        print('Você escolheu: SOMA')                     #lembrar de proibir numeros negativos
        print('Digite o primeiro valor')
        valor1 = input()
        print('Digite o segundo valor')                         
        valor2 = input()
        resultado1 = int(valor1) + int(valor2)
        print(f'O resultado da soma é igual á: {resultado1}')
        print('fim de operação')
        quit()                              #corrigir o quit() programa fechando aruptameente
    
    # Operação de subtração
    if operação < int(3):
        print('Você escolheu: SUBTRAÇÃO')
        print('Digite o primeiro valor')
        valor3 = input()
        print('Digite o segundo valor')
        valor4 = input()
        resultado2 = int(valor3) - int(valor4)
        print(f'O resultado da sua divisão é igual á: {resultado2}')
        print('fim de operação')    
        quit()
    # Operação de Divisão
    elif operação < int(4):
        print('Você escolheu: DIVISÃO')
        print('Digite o primeiro valor')
        valor5 = input()
        print('Digite o segundo valor')
        valor6 = input()
        resultado3 = int(valor5) / int(valor6)
        print(f'O resultado da sua divisão é igual á: {resultado3}')
        print('fim de operação')
        quit()
    # Operação de multiplicação
    elif operação < int(5):
        print('Você escolheu: MULTIPLICAÇÃO')
        print('Digite o primeiro valor')
        valor7 = input()
        print('Digite o segundo valor')
        valor8 = input()
        resultado4 = int(valor7) * int(valor8)
        print(f'O resultado da sua multiplicação é igual á: {resultado4}')
        print('fim de operação')
        quit()
    # Ivalidação do código
    elif operação < int(1):
        print('Número inváido')
        quit()
    else:
        print('Operação inválida')
    
# Call calculate() outside of the function
calculate()

...
def again():
    calc_again = input('''
Deseja calcular novamente?
digite 1 para calcular ou 2 para cancelar.
''')

    # Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == '1':
        calculate()

    # Accept 'n' or 'N' by adding str.upper()
    elif calc_again.upper() == '2':
        print('See you later.')

    else:
        again()
...
