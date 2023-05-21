condiçãodepagamento=int(input('Informe qual será a condição de pagamento: 1 - à vista dinheiro/pix, 2 - à vista no cartão, 3 - em até 2x no cartão e 4 - 3x ou mais no cartão: '))
valor=int(input('Informe o valor: '))
if condiçãodepagamento == 1: 
    valorfinal=valor*0.9
elif condiçãodepagamento == 2:
    valorfinal=valor*0.95
elif condiçãodepagamento == 3:
    valorfinal=valor
elif condiçãodepagamento == 4:
    valorfinal=valor*1.2

print('Valor final: {}'.format(valorfinal))
