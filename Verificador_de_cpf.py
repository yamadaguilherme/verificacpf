from Verificador_input import recebe
from Verificador_processo import processo

def main():
    cpf_filtrado, verificadores = recebe()
    resultado = processo(cpf_filtrado, verificadores)
    print(resultado)

main()