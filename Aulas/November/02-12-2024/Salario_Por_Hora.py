print('\n\nNeste programa vamos ver o quanto você está recebendo no Mês, por Quinzena, por Semana, por Dia, por Hora, e por Minuto! ')
salario = 0
salario = float(input('Digite aqui seu salario que você recebe no Mês, eu cuidarei do resto: '))
horas_trabaladas = int(input('Quantas horas você trabalha no Mês: '))

mes = salario / 1
quinzena = salario / 2
semana = salario / 4
dia = salario / 30
hora = salario / horas_trabaladas
minuto = salario / (horas_trabaladas * 60)


print(f'\n No Mês você recebe R$ {salario}, trabalhando {horas_trabaladas} horas por Mês! ')
print(f'\n Recebendo na Quinzena R$ {quinzena}')
print(f'\n Recebendo na Semana R$ {semana} ')
print(f'\n Recebendo no Dia R$ {dia}  ')
print(f'\n Recebendo na Hora R$ {hora} ')
print(f'\n Recebendo no Minuto R$ {minuto}  ')
