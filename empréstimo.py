valordacasa=float(input('Informe o valor da casa'))
salario=float(input('Informe o salario'))
tempo=int(input('Informe o tempo em anos'))
prestação=valordacasa/(tempo*12)
if (prestação>30/100*salario):
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')
