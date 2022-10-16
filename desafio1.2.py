nome=str(input('Digite seu nome completo: ')).strip().title()
curso=str(input('Digite o nome do curso: ')).upper()
if(curso == 'SI'):
    curso = 'Sistemas de Informação'
if(curso == 'SISTEMA'):
    curso = 'Sistemas de Informação'
elif(curso == 'SISTEMAS'):
    curso = 'Sistemas de Informação'
periodo=int(input('Digite o período que está cursando: '))
primeiraNota=float(input('Digite o valor da primeira nota: '))
segundaNota=float(input('Digite o valor da segunda nota: '))
faltas = int(input('Digite a quantidade de faltas: '))
if(faltas>=11):
    faltas = int(input('Quantidade de faltas deve está entre 0 e 10. Digite novamente a quantidade de faltas: '))

media=float((primeiraNota+segundaNota)/2)
print()

print('Nome: {}'.format(nome))
print('Curso: {}'.format(curso))
print('Período: {}º'.format(periodo))
print('Número de Faltas: {}'.format(faltas))
print('Primeira Nota: {} \nSegunda Nota: {}'.format(primeiraNota,segundaNota))
print('Média das Notas: {:.1f}'.format(media))

print()

if(media>=7) & (faltas<3):
    print('\033[2;36;40mAluno aprovado.\033[m')
else:
    print('\033[2;31;40mAluno reprovado.\033[m')

if(media<7) & (faltas<3):
    print('\033[4;31mReprovado porque não atingiu a média mínima.\033[m')
elif(media>=7) & (faltas>=3):
    print('\033[4;31mReprovado porque excedeu o número de faltas.\033[m')
elif(media<7) & (faltas>=3):
    print('\033[4;31mReprovado porque não atingiu a média mínima e excedeu o número de faltas.\033[m')
