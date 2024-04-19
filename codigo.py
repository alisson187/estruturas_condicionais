while True:
    try:
        salario = float(input('VALOR DO SALARIO: '))
        break
    except:
        print('DADOS ERRADOS TENTE NOVAMENTE')
if salario <= 280:
    novo_salario = salario + (salario * 20 / 100)
    percentual_aplicado = novo_salario - salario
    inflacao = 3.8
    valor_inflacao = novo_salario * (inflacao / 100)
    deconto_inflacao = novo_salario - valor_inflacao
    print('=======================================')
    print('PERCENTUAL APLICADO: => 20% DE AUMENTO')
elif salario > 280 and salario <= 700:
    novo_salario = salario + (salario * 15 / 100)
    percentual_aplicado = novo_salario - salario
    inflacao = 3.8
    valor_inflacao = novo_salario * (inflacao / 100)
    deconto_inflacao = novo_salario - valor_inflacao
    print('========================================')
    print('PERCENTUAL APLICADO: => 15% DE AUMENTO')
elif salario > 700 and salario < 1500:
    novo_salario = salario + (salario * 10 / 100)
    percentual_aplicado = novo_salario - salario
    inflacao = 3.8
    valor_inflacao = novo_salario * (inflacao / 100)
    deconto_inflacao = novo_salario - valor_inflacao
    print('=======================================')
    print('PERCENTUAL APLICADO: => 10% DE AUMENTO')
else:
    novo_salario = salario + (salario * 5 / 100 )
    percentual_aplicado = novo_salario - salario
    inflacao = 3.8
    valor_inflacao = novo_salario * (inflacao / 100)
    deconto_inflacao = novo_salario - valor_inflacao
    print('=======================================')
    print('PERCENTUAL APLICADO: => 5% DE AUMENTO')
    
print(f'SALARIO ANTES DO REAJUSTE => {salario}R$\nVALOR DE AUMENTO => {percentual_aplicado:.2f}R$')
print(f'NOVO SALARIO APOS O AUMENTO => {novo_salario}R$\nVALOR DO AUMENTO REAL APOS O DESCONTO DA INFLAÇAO => {deconto_inflacao:.2f}R$')