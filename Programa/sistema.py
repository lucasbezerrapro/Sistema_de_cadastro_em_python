from lib.interface import *
from time import sleep
from lib.arquivo import *

arquivo = "CADASTRO SISTEMATIZADO DE PESSOAS.txt"

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = Menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        cabeçalho('opcao 1')
        #opcao pra criar o conteudo de um arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        #Cadastrar uma nova pessoa.
        cabeçalho('Novo cadastro')
        nome = str(input('NOME:'))
        idade = leiaInt('IDADE: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[36mSaindo do sistema...\033[m')
        sleep(2.4)
        print('ATE LOGO!')
        break
    else:
        #Digitar uma opcao errada no menu
        print('\033[31mERRO! Digite uma alternativa valida!\033[m')
        sleep(2)