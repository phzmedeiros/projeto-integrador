from banco import Database
from colorama import init, Fore, Style
import os

is_checked = False

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    from tela_boas_vindas import tela_boas_vindas  # Importação local para evitar ciclo
    limpar_tela()
    titulo_ascii = Fore.GREEN + Style.BRIGHT +"""
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

    while not is_checked:
        email = input(Fore.CYAN + "→ E-mail ou usuário: " + Style.RESET_ALL)
        if email == "0":
            tela_boas_vindas()
            return
        senha = input(Fore.CYAN + "→ Senha: " + Style.RESET_ALL)
        if senha == "0":
            tela_boas_vindas()
            return
        check_login(email, senha)

    print(Fore.BLUE + "\nVerificando credenciais...")

def check_login(email, senha):
    db = Database()
    user = db.fetchone("SELECT * FROM tb_client WHERE cli_email = %s AND cli_password = %s", (email, senha))
    db.close()

    if user:
        is_checked = True
        print(Fore.GREEN + "\n✅ E-mail válido. Acesso permitido.\n")
        input(Fore.WHITE + Style.BRIGHT + "\nPressione Enter para continuar...")
    else:
        print(Fore.RED + "\n❌ E-mail inválido. Tente novamente.\n")