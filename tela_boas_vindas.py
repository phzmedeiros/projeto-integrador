import os # Importando a biblioteca os para interações com o sistema operacional
from colorama import Fore, Style, init # Importando a biblioteca colorama para formatação de texto
from login import login # Importando a função de login
from cadastro import cadastro # Importando a função de cadastro

init(autoreset=True) # Iniciar colorama

# Definindo a função que limpa a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Definindo a função que exibe a tela de boas-vindas
def tela_boas_vindas():
    limpar_tela()

    # ASCII art para o título
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
    menu_lateral = Fore.YELLOW + r"""
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Para acessar ao sistema, selecione abaixo uma das opções disponíveis.  │
 │ Com as próximas telas a interação é a mesma, fique livre e bom uso!    │
 └────────────────────────────────────────────────────────────────────────┘
""" # Exibindo o menu lateral e instruções para o usuário
    
    # Definindo as opções do menu
    opcoes = Fore.CYAN + Style.BRIGHT + r"""
┌───────────────┐
│ Opções:       │
│               │
│ [1] Login     │
│ [2] Cadastrar │
│ [0] Sair      │
└───────────────┘
"""

    print(titulo_ascii + menu_lateral + opcoes)
    while True: # Loop para garantir que o usuário escolha uma opção válida
        # Solicita ao usuário que escolha uma opção
        opcao = input(Fore.WHITE + Style.BRIGHT + "Digite a opção escolhida: ")
        if opcao == "1": # Se o usuário digitar "1": inicia o processo de login
            login()
            break
        elif opcao == "2": # Se o usuário digitar "2": inicia o processo de cadastro
            cadastro()
            break
        elif opcao == "0": # Se o usuário digitar "3": encerra o programa
            print(Fore.GREEN + "Até logo!")
            break
        else: # Se o usuário digitar uma opção inválida: exibe mensagem de erro
            print(Fore.RED + "Opção inválida. Tente novamente.")