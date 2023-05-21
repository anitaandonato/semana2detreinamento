import random

print ('Pedra, Papel ou Tesoura')
print ('Escolha uma opção:')
print ('1. Pedra')
print ('2. Papel')
print ('3. Tesoura')
print ('4. Sair')

escolhido_pelo_usuario= int(input('Digite sua escolha: '))
while(escolhido_pelo_usuario!=4):
    escolhido_pelo_computador=random.randint(1,3)
    opções=["Pedra","Papel","Tesoura"]

    print ('Você escolheu: {}'.format(opções[escolhido_pelo_usuario-1]))
    print ('O computador escolheu: {}'.format(opções[escolhido_pelo_computador - 1]))

    if escolhido_pelo_usuario == escolhido_pelo_computador:
            print ("Empate!")
    elif (escolhido_pelo_usuario==1 and escolhido_pelo_computador==3) or \
        (escolhido_pelo_usuario==2 and escolhido_pelo_computador==1) or \
        (escolhido_pelo_usuario==3 and escolhido_pelo_computador==2):
            print("Você ganhou!!")
    else:
        print('O computador ganhou!')
    escolhido_pelo_usuario= int(input('Digite sua escolha: '))
print ('Obrigado por jogar')
