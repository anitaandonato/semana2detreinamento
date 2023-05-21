from datetime import date
atual=date.today().year
contador=0
i=1
for i in range(1,8):
    anodenascimento=int(input('Informe o ano de nascimento da pessoa {}'.format(i)))
    idade=atual-anodenascimento
    if idade>=18:
        contador+=1
   
print('A quantidade de pessoas maiores de idade: {}'.format(contador))

