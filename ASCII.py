from tabulate import tabulate

def Ascii(inicial=0, final=None, intervalo=abs(1)):
    # Inserindo o cabeçalho
    cabecalho = ["CHARACTER", "DECIMAL", "OCTAL", "HEXADECIMAL", "BINÁRIO"]
    
    # Inserindo caracteres especiais, que o Python não interpreta de forma que o usuário entenda
    # Inserindo um "", para que assim na contagem, NULL possa ser iniciado em 0,
    # mas é o primeiro valor de uma lista de 33, ou seja, 32 índices
    caracteres_especiais = ["", "NULL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL",
                            "BS", "HT", "NL", "VT", "NP", "CR", "SO", "SI", "DLE",
                            "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN",
                            "EM", "SUB", "ESC", "FS", "GS", "RS", "US", "SPACE"]

    caracteres_especiais2 = ["", "del", "Ç", "ü", "é", "â", "ä", "à", "å", "ç", "ê", "ë", "è", "ï", "î", "ì",
                             "Ä", "Å", "É", "æ", "Æ", "ô", "ö", "ò", "û", "ù", "ÿ", "Ö", "Ü", "ø", "£", "Ø", "ƒ", "á", "í"]

    dados = []  # Inicializa a lista de dados

    if intervalo == 0:
        print("Não é possível realizar a busca com um intervalo de zero!")

    if final:
        for asc in range(inicial, final + 1, intervalo):
            if 127 <= asc <= 160:
                try:
                    char = caracteres_especiais2[(asc - 127) + 1]
                except:
                    pass
            elif asc <= 32:
                char = caracteres_especiais[asc+1]
            else:
                char = chr(asc)
            dado = [
                char,
                asc,
                oct(asc),
                hex(asc),
                bin(asc)
            ]
            dados.append(dado)
    else:
        if 127 < inicial < 160:
            char = caracteres_especiais2[(inicial - 127) + 1]
        elif inicial < 32:
            char = caracteres_especiais[inicial+1]
        else:
            char = chr(inicial)
        dado = [
            char,
            inicial,
            oct(inicial),
            hex(inicial),
            bin(inicial)
        ]
        dados.append(dado)

    print(tabulate(dados, headers=cabecalho, tablefmt="grid", stralign="center"))

if __name__ == "__main__":
    print("BEM VINDO!")
    Ascii(0, 190)  # Fique à vontade para verificar os dados e mudar os valores
