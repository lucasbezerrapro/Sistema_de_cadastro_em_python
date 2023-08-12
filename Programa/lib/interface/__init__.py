def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TabError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[033[m')
            return 0
        else:
            return n

def linha(tam=42):
    return '-'*42

def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def Menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1 
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c+=1
    print(linha())
    opc = leiaInt('Sua escolha: ')
    return opc


