n1=float(input('Informe o valor do primeiro numero: '))
n2=float(input('Informe o valor do segundo numero: '))
maior=0
opção=0



while (opção!=5):
    print ('1. somar')
    print ('2. multiplicar')
    print ('3. maior')
    print ('4. novos números')
    print ('5. sair do programa')

    opção=int(input('Digite a opção que deseja: '))

    if (opção==1):
        soma=n1+n2
        print ('Valor da soma: {}'.format(soma))
    if (opção==2):
        multiplicar=n1*n2
        print ('Valor da multiplicação: {}'.format(multiplicar))
    if (opção==3):
        if (n1>n2):
            maior=n1
            print ('O maior numero é o primeiro: {}'.format(maior))
        elif(n2>n1):
            maior=n2
            print('O maior numero é o segundo: {}'.format(maior))
        else:
            print('Os dois números são iguais')
    if (opção==4):
        n1=float(input('Informe o valor do primeiro numero: '))
        n2=float(input('Informe o valor do segundo numero: '))

print ('Obrigado por jogar!')
