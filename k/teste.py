import os
os.system('cls')
while True:
    print()
    print(30 * '=' , 'CALCULADORA', 30 * '=')
    print('1. adição')
    print('2. subtração')
    print('3. multiplicação')
    print('4. divisão')
    print('5. sair')
    print(73 * '=')

    opcao = input('digite uma opcão:')

    if opcao == '1':
        os.system('cls')
        while True:    
            num1 = int(input('digite um numero para somar:'))
            num2 = int(input('digite outro numero para somar:'))
            soma = num1 + num2
            print(f'o resultado é:{soma}')
            print('1. para somar denovo')
            print('2. para voltar')
            opcao = input('digite uma opcão:')
            if opcao == '1':
                print('blz chefe')
            elif opcao == '2':
                os.system('cls')
                break
            else:
                print('digite alguma opção!!')
                break
   
   
    elif opcao == '2':
        os.system('cls')
        while True:
            num1 = int(input('digite um numero para subtrair:'))
            num2 = int(input('digite outro numero para subtrair:'))
            dimi = num1 - num2
            print(f'o resultado é: {dimi}')
            print('1. para diminuir denovo')
            print('2. para voltar')
            opcao = input('digite uma opcão:')
            if opcao == '1':
                print('blz chefe')
            elif opcao == '2':
                os.system('cls')
                break
            else:
                print('digite alguma opção!!')
                break
  
  
    elif opcao == '3':
        os.system('cls')
        while True:
            num1 = int(input('digite um numero para multiplicar:'))
            num2 = int(input('digite outro numero para multiplicar:'))
            multi = num1 * num2
            print(f'o resultado é: {multi}')
            print('1. para multiplicar denovo')
            print('2. para voltar')
            opcao = input('digite uma opcão:')
            if opcao == '1':
                print('blz chefe')
            elif opcao == '2':
                os.system('cls')
                break
            else:
                print('digite alguma opção!!')
                break

    
    elif opcao == '4':
         os.system('cls')
         while True:
            num1 = float(input('digite um numero para dividir:'))
            num2 = float(input('digite outro numero para dividir:'))
            divi = num1 / num2
            print(f'o resultado é: {divi:.2f}')
            print('1. para dividir denovo')
            print('2. para voltar')
            opcao = input('digite uma opcão:')
            if opcao == '1':
                print('blz chefe')
            elif opcao == '2':
                os.system('cls')
                break
            else:
                print('digite alguma opção!!')
                break
              
    elif opcao == '5':
        print('saindo...')
        break

    else:
        print('digite alguma opção!!')