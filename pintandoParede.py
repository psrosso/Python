larg = float(input('Insira a largura da parede: '))
alt = float(input('Insira a altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {:.0f}x{:.0f} e sua área é de {}m²'.format(
    larg, alt, área))
tinta = área / 2
print('Para pintar sua parede, você irá precisar de {}L de tinta.'.format(tinta))
