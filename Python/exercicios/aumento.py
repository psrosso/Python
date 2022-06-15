salario = float(input('Você foi promovido e receberá um aumento de 15% no seu salário!! \nPara o reajuste, insira seu salário atual: R$'))
aumento = salario + (salario * 15 / 100)
print('De acordo com sua promoção, seu salário será reajustado para: R${}'.format(aumento))