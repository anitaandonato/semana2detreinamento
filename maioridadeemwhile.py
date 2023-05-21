from datetime import date
atual=date.today().year
contador=0
pessoas=1
while pessoas<=7:
    ano=int(input('Informe o ano de nascimento da pessoa {}: '.format(pessoas)))
    idade=atual-ano
    if idade>=18:
        contador+=1
    pessoas+=1
print('Quantidade de pessoas maiores de idade:{}'.format(contador))