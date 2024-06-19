num_funcionario = (input())
salario_funcionario = float(input())
vendas_funcionario = float(input())

salario = salario_funcionario + (vendas_funcionario * 0.15)


print('TOTAL = R$ {:.2f}'.format(salario))