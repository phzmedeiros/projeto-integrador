import os
from colorama import Fore, Style, init
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def tela_boas_vindas():
    limpar_tela()

# título
    titulo_ascii = Fore.GREEN + r"""                                                                                            
@@@@@@@    @@@@@@    @@@@@@    @@@@@@      @@@  @@@  @@@  @@@  @@@  @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@      @@@  @@@  @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@!  @@@  @@!  @@@  !@@          @@!  @@@  @@!  @@!@!@@@  @@!  @@@  @@!  @@@  !@@       
!@   @!@  !@!  @!@  !@!  @!@  !@!          !@!  @!@  !@!  !@!!@!@!  !@!  @!@  !@!  @!@  !@!       
@!@!@!@   @!@  !@!  @!@!@!@!  !!@@!!       @!@  !@!  !!@  @!@ !!@!  @!@  !@!  @!@!@!@!  !!@@!!    
!!!@!!!!  !@!  !!!  !!!@!!!!   !!@!!!      !@!  !!!  !!!  !@!  !!!  !@!  !!!  !!!@!!!!   !!@!!!   
!!:  !!!  !!:  !!!  !!:  !!!       !:!     :!:  !!:  !!:  !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:  !:!  :!:  !:!      !:!       ::!!:!   :!:  :!:  !:!  :!:  !:!  :!:  !:!      !:!   
 :: ::::  ::::: ::  ::   :::  :::: ::        ::::     ::   ::   ::   :::: ::  ::   :::  :::: ::   
:: : ::    : :  :    :   : :  :: : :          :      :    ::    :   :: :  :    :   : :  :: : :                                                                                                      
"""

    menu_lateral = Fore.WHITE + """
 ┌────────────────────────────────────────────────┐
 │ Aplicação para desenvolvimento sustentável.    │
 │ Análise de dados e mentoria pra uma melhor     │
 │ sustentabilidade e uma melhor rotina pessoal   │
 └────────────────────────────────────────────────┘
"""
 # Opções do menu
    opcoes = Fore.YELLOW + Style.BRIGHT + """
 [1] Login
 [2] Cadastrar
 [3] Sair
"""

    print(titulo_ascii + menu_lateral + opcoes)

    while True: # Loop para capturar a opção do usuário
        opcao = input(Fore.CYAN + "\nEscolha uma opção: ")
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
            print(Fore.RED + "❌ Opção inválida. Tente novamente.")
