import os
from colorama import Fore, Style, init
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    limpar_tela()

    titulo_ascii = Fore.GREEN + Style.BRIGHT + """
 _   _       _     _ _   _____                           _                 _       
| | | |     | |   (_) | |  __ \                      │  | |               (_)       
| |_| | __ _| |__  _| |_| |  \/_ __ ___  ___ _ __    │  | |     ___   __ _ _ _ __  
|  _  |/ _` | '_ \| | __| | __| '__/ _ \/ _ \ '_ \   │  | |    / _ \ / _` | | '_ \ 
| | | | (_| | |_) | | |_| |_\ \ | |  __/  __/ | | |  │  | |___| (_) | (_| | | | | |
\_| |_/\__,_|_.__/|_|\__|\____/_|  \___|\___|_| |_|  │  \_____/\___/ \__, |_|_| |_|
                                                                      __/ |        
                                                                     |___/         
""" + Fore.YELLOW + """
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │ Faça seu login para acessar o HabitGreen.                                              │
 │ Digite suas credenciais (email e senha) ou pressione [0] para voltar à tela inicial.   │
 └────────────────────────────────────────────────────────────────────────────────────────┘
"""
    print(titulo_ascii)

    email = input(Fore.CYAN + "→ E-mail ou usuário: " + Style.RESET_ALL)
    if email == "0":
        return
    
    senha = input(Fore.CYAN + "→ Senha: " + Style.RESET_ALL)
    if senha == "0":
        return

    # Aqui vai a verificação futura no banco de dados
    print(Fore.BLUE + "\nVerificando credenciais...")

    # Simulação de login bem-sucedido
    print(Fore.GREEN + "\nLogin realizado com sucesso!")
    input(Fore.WHITE + Style.BRIGHT + "\nPressione Enter para continuar...")
