# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velo = float(input('Velocidade atual do veículo (Km/h): '))
if velo > 80:
    print('Velocidade máxima permitida: 80Km/h. \nVelocidade do veículo: {:.2f}Km/h'.format(velo))
    print('Velocidade excedida: {:.2f}Km/h. \nO valor da multa é de R${:.2f}.'.format((velo - 80), float((velo - 80) * 7)))
else:
    print('Velociadade do veículo dentro do valor permitido. \nTenha um bom dia! Dirija com segurança.')
