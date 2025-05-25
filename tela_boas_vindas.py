import os # importando a biblioteca os para conseguir limpar a tela
from colorama import Fore, Style, init # importando a biblioteca colorama para conseguir colorir o terminal
from login import login # importando a função de login
from cadastro import cadastro # importando a função de cadastro

init(autoreset=True) # inicializando a biblioteca colorama para que as cores sejam resetadas automaticamente

# Função para limpar a tela do terminal
def limpar_tela(): 
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir a tela de boas-vindas
def tela_boas_vindas():
    # Limpa a tela chamando a função limpar_tela
    limpar_tela()
    # define o título da tela de boas-vindas utilizando caracteres ASCII e colorindo com o colorama
    titulo_ascii = Fore.GREEN + Style.BRIGHT + r"""                                                                                            
______                      _   _  _             _                             │
| ___ \                    | | | |(_)           | |                            │      Aplicação para desenvolvimento sustentável.
| |_/ /  ___    __ _  ___  | | | | _  _ __    __| |  __ _  ___                 │      Análise de dados e mentoria pra uma melhor
| ___ \ / _ \  / _` |/ __| | | | || || '_ \  / _` | / _` |/ __|                │      sustentabilidade e uma melhor rotina pessoal.
| |_/ /| (_) || (_| |\__ \ \ \_/ /| || | | || (_| || (_| |\__ \                │ 
\____/  \___/  \__,_||___/  \___/ |_||_| |_| \__,_| \__,_||___/                │      Desenvolvido por:
                _   _         _      _  _    _____                             │      Alinne Monteiro de Melo
               | | | |       | |    (_)| |  |  __ \                            │      Alycia Santos Bond
  __ _   ___   | |_| |  __ _ | |__   _ | |_ | |  \/ _ __  ___   ___  _ __      │      Pedro Henrique Medeiros dos Reis
 / _` | / _ \  |  _  | / _` || '_ \ | || __|| | __ | '__|/ _ \ / _ \| '_ \     │      Rafael Antônio Candian 
| (_| || (_) | | | | || (_| || |_) || || |_ | |_\ \| |  |  __/|  __/| | | |    │
 \__,_| \___/  \_| |_/ \__,_||_.__/ |_| \__| \____/|_|   \___| \___||_| |_|    │      Pontifícia Universidade Católica de Campinas
                                                                               │
"""
    # Define o menu lateral com opções de login e cadastro
    menu_lateral = Fore.YELLOW + r"""
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Para acessar ao sistema, selecione abaixo uma das opções disponíveis.  │
 │ Com as próximas telas a interação é a mesma, fique livre e bom uso!    │
 └────────────────────────────────────────────────────────────────────────┘
"""
    # Define as opções disponíveis no menu
    opcoes = Fore.CYAN + Style.BRIGHT + r"""
┌───────────────┐
│ Opções:       │
│               │
│ [1] Login     │
│ [2] Cadastrar │
│ [0] Sair      │
└───────────────┘
"""

    # Exibe o título, menu lateral e opções no terminal
    print(titulo_ascii + menu_lateral + opcoes)
    
    # Loop para receber a opção do usuário e tratar erros de entrada
    while True:
        # Solicita ao usuário que digite a opção escolhida
        opcao = input(Fore.WHITE + Style.BRIGHT + "Digite a opção escolhida: ")
        # se o usuário digitar 1, chama a função de login
        if opcao == "1":
            login()
            break
        # se o usuário digitar 2, chama a função de cadastro
        elif opcao == "2":
            cadastro()
            break
        # se o usuário digitar 0, exibe uma mensagem de despedida e encerra o loop
        elif opcao == "0":
            print(Fore.GREEN + "Até logo!")
            break
        # se o usuário digitar uma opção inválida, exibe uma mensagem de erro
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")