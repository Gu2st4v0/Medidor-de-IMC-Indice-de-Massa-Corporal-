print('Olá, sou o seu medidor de IMC (Indice de Massa Corporal), vamos lá...')
print(' ')
print('-=-' * 17)
print(' ')
nome = str(input('Digite seu nome: '))
print(' ')
print('olá senhor(a) {}, para calcularmos seu IMC conhecido como indice de Massa Corporal vamos precisar do seu tamanho em metros e seu peso em kilograma. '.format((nome)))
print(' ')
print('Coloque abaixo seu peso e seu tamanho porfavor senhor(a) {}.'.format((nome)))
print(' ')
peso = float(input('Digite seu peso:(kg) '))
tamanho = float(input('Digite seu tamanho em Metros:(M) '))

imc = peso / (tamanho ** 2)

if imc <= 18.5:
    print('Seu IMC é de {:.2f} senhor {}, que é classificado como abaixo do peso, você necessita ganhar peso, atente-se !'.format((imc), (nome)))

elif imc <= 24.9:
    print('Seu IMC é de {:.2f} senhor {}, que é classificado como peso normal !'.format((imc), (nome)))

elif imc <= 29.9:
    print('Seu IMC é de {:.2f} senhor {}, que é classificado como sobrepeso !'.format((imc), (nome)))

elif imc <= 34.9:
    print('Seu IMC é de {:.2f} senhor {}, que é classificado como obesidade grau I. Atente-se !'.format((imc), (nome)))

elif imc <= 39.9:
    print('Seu IMC é de {:.2f} senhor {}, que é classificado como obesidade grau II. Atente-se !'.format((imc), (nome)))
    
elif imc > 40:
    print('Seu IMC é de {:.2f} senhor {}, que é classificado como obesidade grau III. Atente-se !'.format((imc)))






        