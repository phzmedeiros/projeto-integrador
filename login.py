from banco import Database
from colorama import Fore, Style, init
from menu import menu
from sessao import usuario_logado
import os
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    limpar_tela()
    titulo_ascii = Fore.GREEN + Style.BRIGHT + r"""
 _   _       _     _ _   _____                       │   _                 _       
| | | |     | |   (_) | |  __ \                      │  | |               (_)      
| |_| | __ _| |__  _| |_| |  \/_ __ ___  ___ _ __    │  | |     ___   __ _ _ _ __  
|  _  |/ _` | '_ \| | __| | __| '__/ _ \/ _ \ '_ \   │  | |    / _ \ / _` | | '_ \ 
| | | | (_| | |_) | | |_| |_\ \ | |  __/  __/ | | |  │  | |___| (_) | (_| | | | | |
\_| |_/\__,_|_.__/|_|\__|\____/_|  \___|\___|_| |_|  │  \_____/\___/ \__, |_|_| |_|
                                                     │                __/ |        
                                                     │               |___/         
"""
    menu_lateral = Fore.YELLOW + """
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Faça seu login para acessar o HabitGreen                                               │
│ Digite suas credenciais (email e senha) ou pressione [0] para voltar ao menu inicial   │
└────────────────────────────────────────────────────────────────────────────────────────┘
"""
    print(titulo_ascii + menu_lateral)

    while True:
        from tela_boas_vindas import tela_boas_vindas
        email = input(Fore.CYAN + "→ E-mail: " + Style.RESET_ALL).strip()
        if email == "0":
            tela_boas_vindas()
            return
        
        senha = input(Fore.CYAN + "→ Senha: " + Style.RESET_ALL).strip()
        if senha == "0":
            tela_boas_vindas()
            return

        if check_login(email, senha):
            from menu import menu
            limpar_tela()
            print(Fore.GREEN + Style.BRIGHT + "\nLogin realizado com sucesso!")
            limpar_tela()
            menu()
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nE-mail ou senha inválidos. Tente novamente.\n")

def check_login(email, senha):
    db = Database()
    user = db.fetchone("SELECT * FROM tb_client WHERE cli_email = %s AND cli_password = %s", (email, senha))
    db.close()

    if user:
        usuario_logado["id"] = user[0]
        usuario_logado["nome"] = user[1]
        usuario_logado["email"] = user[2]
        return True
    return False