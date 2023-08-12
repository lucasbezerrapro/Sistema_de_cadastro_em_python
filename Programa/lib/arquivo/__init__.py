from lib.interface import *

def arquivoExiste(nome_do_arquivo):
    try:
        a = open(nome_do_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome_do_arquivo):
    try:
        a = open(nome_do_arquivo, 'wt+')
    except:
        print('Houve um erro ao criar arquivo.')
    else:
        print('Arquivo criado com sucesso.')
def lerArquivo(nome_do_arquivo):
    try:
        a = open(nome_do_arquivo, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

        
        # criar um contador
def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a= open(arquivo, 'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao cadastrar pessoas')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()