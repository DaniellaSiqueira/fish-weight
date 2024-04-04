peso = int(input('Digite a quantidade de kgs pescados: '))
excesso = peso % 50 
multa = excesso * 4
if excesso * 4:
    print (f'Excesso: {excesso}kgs. Você foi multado em: R${multa} ')
else:
    print (f'Excesso: {excesso}kgs. Você não foi multado! ')
