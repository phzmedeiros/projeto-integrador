import os
from colorama import Fore, Style, init
init(autoreset=True) # Iniciar colorama


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def tela_boas_vindas():
    limpar_tela()

# título com arte ASCII
    titulo_ascii = Fore.GREEN + Style.BRIGHT +"""                                                                                            
______                      _   _  _             _                             │
| ___ \                    | | | |(_)           | |                            │      Aplicação para desenvolvimento sustentável.
| |_/ /  ___    __ _  ___  | | | | _  _ __    __| |  __ _  ___                 │      Análise de dados e mentoria pra uma melhor
| ___ \ / _ \  / _` |/ __| | | | || || '_ \  / _` | / _` |/ __|                │      sustentabilidade e uma melhor rotina pessoal.
| |_/ /| (_) || (_| |\__ \ \ \_/ /| || | | || (_| || (_| |\__ \                │ 
\____/  \___/  \__,_||___/  \___/ |_||_| |_| \__,_| \__,_||___/                │      Desenvolvido por:
                _   _         _      _  _    _____                             │      Alinne Monteiro de Melo
               | | | |       | |    (_)| |  |  __ \                            │      Alycia dos Santos Bond
  __ _   ___   | |_| |  __ _ | |__   _ | |_ | |  \/ _ __  ___   ___  _ __      │      Pedro Henrique Medeiros
 / _` | / _ \  |  _  | / _` || '_ \ | || __|| | __ | '__|/ _ \ / _ \| '_ \     │      Rafael Antônio Candian 
| (_| || (_) | | | | || (_| || |_) || || |_ | |_\ \| |  |  __/|  __/| | | |    │
 \__,_| \___/  \_| |_/ \__,_||_.__/ |_| \__| \____/|_|   \___| \___||_| |_|    │      Pontifícia Universidade Católica de Campinas
                                                                               │
"""

# menu lateral com informações para o usuário
    menu_lateral = Fore.YELLOW + """
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Para acessar ao sistema, selecione abaixo uma das opções disponíveis.  │
 │ Com as próximas telas a interação é a mesma, fique livre e bom uso!    │
 └────────────────────────────────────────────────────────────────────────┘
"""

    opcoes = Fore.CYAN + Style.BRIGHT + """
┌───────────────┐
│ Opções:       │
│               │
│ [1] Login     │
│ [2] Cadastrar │
│ [3] Sair      │
└───────────────┘
"""

    print(f"{titulo_ascii}{menu_lateral}" + opcoes)

    while True: # loop para verificar a opção escolhida
        opcao = input(Fore.WHITE + Style.BRIGHT + "Digite a opção escolhida: ")
        if opcao == "1":
            from login import login
            login()
            break
        elif opcao == "2":
            from cadastro import cadastro
            cadastro()
            break
        elif opcao == "3":
            print(Fore.GREEN + "Até logo!")
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")
