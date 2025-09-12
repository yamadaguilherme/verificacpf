from verificador_input import recebe
from verificador_processo import processo

def main():
    cpf_filtrado, verificadores = recebe()
    resultado = processo(cpf_filtrado, verificadores)
    print(resultado)


main()
