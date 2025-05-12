import os
import re
from colorama import init, Fore, Style


from banco import Database
from criptografia import cifra_hill_criptografar, cifra_hill_descriptografar, CHAVE_HILL
init(autoreset=True)  # Iniciar colorama

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11


def cadastro():
    from tela_boas_vindas import tela_boas_vindas
    while True:
        
        limpar_tela()
        
        titulo_ascii = Fore.GREEN + Style.BRIGHT + r"""
 _   _       _     _ _   _____                       │   _____           _           _       
| | | |     | |   (_) | |  __ \                      │  /  __ \         | |         | |      
| |_| | __ _| |__  _| |_| |  \/_ __ ___  ___ _ __    │  | /  \/ __ _  __| | __ _ ___| |_ _ __ ___  
|  _  |/ _` | '_ \| | __| | __| '__/ _ \/ _ \ '_ \   │  | |    / _` |/ _` |/ _` / __| __| '__/ _ \ 
| | | | (_| | |_) | | |_| |_\ \ | |  __/  __/ | | |  │  | \__/\ (_| | (_| | (_| \__ \ |_| | | (_) |
\_| |_/\__,_|_.__/|_|\__|\____/_|  \___|\___|_| |_|  │   \____/\__,_|\__,_|\__,_|___/\__|_|  \___/ 
                                                     │
"""   
        menu_lateral = Fore.YELLOW + """
┌────────────────────────────────────────────────────────────────────────┐
│ Para se cadastrar ao HabitGreen você deverá inserir seu nome, email,   │
│ CPF e senha, além de ter também que confirmar-la.                      │
│ Caso precise, pressione [0] para voltar ao menu inicial.               │
└────────────────────────────────────────────────────────────────────────┘
"""
        print(titulo_ascii + menu_lateral)

        # Nome
        while True:
            nome = input("→ Nome: " + Style.RESET_ALL).strip()
            if nome == "0":
                tela_boas_vindas()
                return
            else:
                break

         # E-mail
        while True:
            email = input("→ E-mail: " + Style.RESET_ALL).strip()
            if email == "0":
                tela_boas_vindas()
                return
            if not validar_email(email):
                print(Fore.RED + "\nE-mail inválido. Tente novamente.\n")
                continue
            db = Database()
            ja_existe_email = db.fetchone("SELECT * FROM tb_client WHERE cli_email = %s", (email,))
            db.close()
            if ja_existe_email:
                print(Fore.RED + "\nE-mail já cadastrado. Tente outro.\n")
                continue
            break

        # CPF
        while True:
            cpf = input("→ CPF: " + Style.RESET_ALL).strip()
            if cpf == "0":
                tela_boas_vindas()
                return
            if not validar_cpf(cpf):
                print(Fore.RED + "\nCPF inválido. Deve conter 11 dígitos.\n")
                continue
            db = Database()
            ja_existe_cpf = db.fetchone("SELECT * FROM tb_client WHERE cli_cpf = %s", (cpf,))
            db.close()
            if ja_existe_cpf:
                print(Fore.RED + "\nCPF já cadastrado. Tente outro.\n")
                continue
            break

        # Senha
        while True:
            senha = input("→ Senha: " + Style.RESET_ALL).strip()
            if senha == "0":
                tela_boas_vindas()
                return
            if len(senha) >= 6:
                break
            print(Fore.RED + "\nSenha muito curta. Tente novamente.\n")

        # Confirmação
        while True:
            confirma = input("→ Confirmar Senha: " + Style.RESET_ALL).strip()
            if confirma == "0":
                tela_boas_vindas()
                return
            if senha == confirma:
                break
            print(Fore.RED + "\nAs senhas não coincidem. Tente novamente.\n")
        limpar_tela()
        #registra o usuário no banco de dados
        register_user(nome, email, senha, cpf)
        #voltar para a tela de boas vindas
        tela_boas_vindas()
        break

def register_user(nome, email, senha, cpf):
    # Criptografa a senha antes de salvar
    senha_criptografada = cifra_hill_criptografar(senha, CHAVE_HILL)

    db = Database()
    db.execute("INSERT INTO tb_client (cli_name, cli_email, cli_password, cli_cpf) VALUES (%s, %s, %s, %s)",
               (nome, email, senha_criptografada, cpf))
    print(Fore.GREEN + f"\nCadastro realizado com sucesso para {nome}!\n")
    input(Fore.CYAN + "Pressione [Enter] para continuar...")
