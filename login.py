from banco import Database #Importando a classe Database para interagir com o banco de dados
from colorama import Fore, Style, init #Importando a biblioteca colorama para formatação de cores no terminal
from menu import menu #Importando a função que exibe o menu principal
from sessao import usuario_logado #Importando o dicionário que armazena os dados do usuário logado
import os #Importando a biblioteca os para interações com o sistema operacional

# Iniciar colorama
init(autoreset=True)

# Definindo a função que limpa a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') 

# Definindo a função que exibe a tela de login
def login():
    limpar_tela()
    # ASCII art para o título
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
    # Exibindo o menu lateral e instruções para o usuário
    menu_lateral = Fore.YELLOW + """
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Faça seu login para acessar o HabitGreen                                               │
│ Digite suas credenciais (email e senha) ou pressione [0] para voltar ao menu inicial   │
└────────────────────────────────────────────────────────────────────────────────────────┘
"""
    print(titulo_ascii + menu_lateral)

# Definindo o loop de login
    while True:
        from tela_boas_vindas import tela_boas_vindas #Importando a função que exibe a tela de boas-vindas
        # Solicita o e-mail do usuário
        # Se o usuário digitar "0", retorna à tela de boas-vindas
        email = input(Fore.GREEN + "→ E-mail: " + Style.RESET_ALL).strip()
        if email == "0":
            tela_boas_vindas()
            return
        
        # Solicita a senha do usuário
        # Se o usuário digitar "0", retorna à tela de boas-vindas
        senha = input(Fore.GREEN + "→ Senha: " + Style.RESET_ALL).strip()
        if senha == "0":
            tela_boas_vindas()
            return

# Verifica se o e-mail e a senha são válidos
        if check_login(email, senha):
            from menu import menu #Importando a função que exibe o menu principal
            limpar_tela()
            print(Fore.GREEN + Style.BRIGHT + "\nLogin realizado com sucesso!")
            limpar_tela()
            menu() # Redireciona para o menu principal
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nE-mail ou senha inválidos. Tente novamente.\n")

# Função para verificar as credenciais do usuário no banco de dados
# Recebe o e-mail e a senha como parâmetros
def check_login(email, senha):
    db = Database()
    # Executa uma consulta SQL para verificar se o usuário existe
    user = db.fetchone("SELECT * FROM tb_client WHERE cli_email = %s AND cli_password = %s", (email, senha))
    db.close()

# Se o usuário for encontrado, armazena os dados no dicionário usuario_logado e retorna True
# Se não, retorna False    
    if user:
        usuario_logado["id"] = user[0]
        usuario_logado["nome"] = user[1]
        usuario_logado["email"] = user[2]
        return True
    return False