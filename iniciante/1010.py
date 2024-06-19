codigo1, unid1, valor1= input().split()

codigo2, unid2, valor2 = input().split()


total = (int(unid1)*float(valor1)) + (int(unid2)*float(valor2))

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
