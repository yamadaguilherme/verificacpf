#entrada
cpf = input('Qual o cpf que quer verificar? ')

#formatação para lista e tirar caracteres inuteis
lista_cpf = list(cpf)
quantidade_de_ponto = lista_cpf.count('.')
quantidade_de_traço = lista_cpf.count('-')

#verificacao de modelo inputado
quantia = quantidade_de_ponto == 2 and quantidade_de_traço == 1
números = len(lista_cpf) == 14

#contadores e dados salvos
verif_penultimo = 0
verif_ultimo = 0
verificadores = []
verificadores.insert(0, lista_cpf[13])
verificadores.insert(0, lista_cpf[12])

#algoritmo do penultimo digito
if quantia == True and números == True:
    for i in [13, 12, 11, 7, 3]:
        lista_cpf.pop(i)
    
    for i, num in enumerate(lista_cpf):
        multiplicador = 10 - i
        resultado = multiplicador * int(num)
        verif_penultimo += resultado
    multiplicado = verif_penultimo * 10
    divisor = multiplicado % 11
    penultimo_digito = divisor if divisor <= 9 else 0
    if penultimo_digito == int(verificadores[0]):
        lista_cpf.append(verificadores[0])
        print(f'O seu penúltimo digito do cpf está correto: {verificadores[0]}')
    else:
        print('O seu cpf está incorreto')
        
        #alg do ultimo digito
    for i, num in enumerate(lista_cpf):
        multiplicador = 11 - i
        resultado = multiplicador * int(num)
        verif_ultimo += resultado
    multiplicado = verif_ultimo * 10
    divisor = multiplicado % 11
    ultimo_digito = divisor if divisor <= 9 else 0
    if ultimo_digito == int(verificadores[1]):
        lista_cpf.append(verificadores[1])
        print(f'O seu último digito do cpf está correto: {verificadores[1]}')
    else:
        print('O seu cpf está incorreto')
    if penultimo_digito == int(verificadores[0]) and ultimo_digito == int(verificadores[1]):
        print('CPF está correto!')
else:
    print('O cpf informado é inválido, digite com os pontos e traços.')

