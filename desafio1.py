cdverde = 10.00
cdazul = 20.00
cdamarelo = 30.00
cdvermelho = 40.00

cd=input('Informe a cor do CD que deseja adquirir (\033[1;32mVerde\033[m, \033[1;34mAzul\033[m, \033[1;33mAmarelo\033[m ou \033[1;31mVermelho\033[m) e descubra quanto custa:  ').strip()
cd=cd.lower()

if(cd == 'verde'):
    print('Os CDs verdes custam {:.2f}'. format(cdverde))
elif(cd == 'azul'):
    print('Os CDs azuis custam {:.2f}'.format(cdazul))
elif(cd == 'amarelo'):
    print('Os CDs amarelos custam R$ {:.2f}'.format(cdamarelo))
elif(cd == 'vermelho'):
    print('Os CDs vermelhos custam R$ {:.2f}'.format(cdvermelho))
elif(cd != 'verde, azul, amarelo, vermelho'):
    print('\n\033[7;40mCor de CD inválida!!! Tente novamente.\033[m As cores disponíveis são \033[1;32mVerde\033[m, \033[1;34mAzul\033[m, \033[1;33mAmarelo\033[m e \033[1;31mVermelho\033[m')

print('Teste git e github')

