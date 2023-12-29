from tabulate import tabulate

def Ascii(inicial, final=None, intervalo=abs(1)):
    # Inserindo o cabeçalho
    cabecalho = ["CHARACTER", "DECIMAL", "OCTAL", "HEXADECIMAL", "BINÁRIO"]
    
    # Inserindo caracteres especiais, que o python não interpreta de forma que o usuário entenda
    # Inserindo um "", para que assim na contagem, NULL possa ser iniciado em 0,
    # mas é o primeiro valor de uma lista de 33, ou seja, 32 índices
    caracteres_especiais = ["", "NULL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL",
                            "BS", "HT", "NL", "VT", "NP", "CR", "SO", "SI", "DLE",
                            "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN",
                            "EM", "SUB", "ESC", "FS", "GS", "RS", "US", "SPACE"]

    dados = []  # Inicializa a lista de dados

    if intervalo == 0:
        print("Não é possível realizar a busca com um intervalo de zero!")

    if final:
        for asc in range(inicial, final + 1, intervalo):
            if inicial > 32:
                char = chr(asc)
            elif inicial == 0 and final == 32:
                char = caracteres_especiais[asc + 1]
            else:
                char = chr(asc) if 32 < asc else caracteres_especiais[asc + 1]

            dado = [
                char,
                asc,
                oct(asc),
                hex(asc),
                bin(asc)
            ]
            dados.append(dado)
    else:
        char = chr(inicial) if 32 < inicial else caracteres_especiais[inicial + 1]
        dado = [
            char,
            inicial,
            oct(inicial),
            hex(inicial),
            bin(inicial)
        ]
        dados.append(dado)

    print(tabulate(dados, headers=cabecalho, tablefmt="grid", stralign="center"))

Ascii(0, 32)
