def recebe():
    cpf = input('Qual o cpf que quer verificar? ')
    lista_cpf = list(cpf)

    quantidade_de_ponto = lista_cpf.count('.')
    quantidade_de_traço = lista_cpf.count('-')

    quantia = quantidade_de_ponto == 2 and quantidade_de_traço == 1
    números = len(lista_cpf) == 14

    if quantia and números:
        verificadores = [lista_cpf[12],lista_cpf[13]]
        for i in [11, 7, 3]:
            lista_cpf.pop(i)
        try:
            cpf_filtrado = [int(d) for d in lista_cpf[:-2]]
            return cpf_filtrado, [int(v) for v in verificadores]
        except ValueError:
            print('O CPF informado é inválido.\nCPF possui 11 dígitos.\nExemplo: xxx.yyy.zzz-kk')
            return None, None
    elif len(lista_cpf) == 11 and cpf.isdigit():
        try:
            cpf_filtrado = [int(d) for d in lista_cpf[:-2]]
            verificadores = [int(lista_cpf[-2]), int(lista_cpf[-1])]
            return cpf_filtrado, verificadores
        except:
            print('O CPF informado é inválido.\nCPF possui 11 dígitos.\nExemplo: xxx.yyy.zzz-kk')
            return None, None
