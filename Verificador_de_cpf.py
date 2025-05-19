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
        
def processo(cpf_filtrado, verificadores):
    if not cpf_filtrado or not verificadores:
        return "CPF inválido."
    
    if cpf_filtrado == cpf_filtrado[::-1]:
        return "CPF inválido (números repetidos)."
    
    verif_penultimo = sum((10 - i) * num for i, num in enumerate(cpf_filtrado))
    penultimo = (verif_penultimo * 10) % 11
    penultimo = penultimo if penultimo < 10 else 0
    
    cpf_filtrado.append(penultimo)

    verif_ultimo = sum((11 - i) * num for i, num in enumerate(cpf_filtrado))
    ultimo = (verif_ultimo * 10) % 11
    ultimo = ultimo if ultimo < 10 else 0

    if penultimo == verificadores[0] and ultimo == verificadores[1]:
        return "CPF é válido!"
    else:
        return "CPF inválido."

def main():
    cpf_filtrado, verificadores = recebe()
    resultado = processo(cpf_filtrado, verificadores)
    print(resultado)

main()
