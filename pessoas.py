soma=0
mulheres_antes_dos_vinte=0
idade_homem_mais_velho=0
nome_do_homem_mais_velho=0
for i in range(1,5):
    nome=input('Digite o nome da pessoa {}:  '.format(i))
    idade=int (input('Digite a idade da pessoa {}:  '.format(i)))
    sexo=input('Digite M para masculino e F para feminino:  ')
    soma+=idade
    if sexo.upper()=="F" and idade<20: 
        mulheres_antes_dos_vinte+=1
    if sexo.upper()=="M" and idade>idade_homem_mais_velho:
        idade_homem_mais_velho=idade
        nome_do_homem_mais_velho=nome


media=soma/4

print ('Mulheres antes dos 20: {}'.format(mulheres_antes_dos_vinte)) 
print ('Media de idade: {}'.format(media))
print ('Nome do homem mais velho: {}'.format(nome_do_homem_mais_velho))
