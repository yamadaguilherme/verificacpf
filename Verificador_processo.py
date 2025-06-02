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
