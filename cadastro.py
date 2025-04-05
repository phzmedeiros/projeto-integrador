import os
import re
from colorama import init, Fore, Style
from tela_boas_vindas import tela_boas_vindas
from banco import Database

nome=''
email=''
senha=''
comfirma=''
cpf=''

init(autoreset=True)  # Iniciar colorama

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def cadastro():
    while True:
        limpar_tela()
 
        
        titulo_ascii = Fore.CYAN + Style.BRIGHT +"""
   _____          _           _             
  / ____|        | |         | |            
 | |     __ _  __| | __ _ ___| |_ _ __ ___  
 | |    / _` |/ _` |/ _` / __| __| '__/ _ \ 
 | |___| (_| | (_| | (_| \__ \ |_| | | (_) |
  \_____\__,_|\__,_|\__,_|___/\__|_|  \___/                   
            """
            
        menu_lateral = Fore.YELLOW + """
┌────────────────────────────────────────────────────────────────────────┐
│ Digite [0] para voltar ao menu                                         │
└────────────────────────────────────────────────────────────────────────┘
        """
        print(titulo_ascii,menu_lateral)


        # Nome
        while True:
            nome = input("Nome: \t\t\t" + Style.RESET_ALL).strip()
            if nome == "0":
                tela_boas_vindas()
            else:
                break
            

        # E-mail
        while True:
            email = input("E-mail: \t\t" + Style.RESET_ALL).strip()
            if email == "0":
                tela_boas_vindas()
            if validar_email(email):
                break
            print(Fore.RED + "\n❌ E-mail inválido. Tente novamente.\n")

        # CPF
        while True:
            cpf = input("CPF: \t\t\t" + Style.RESET_ALL).strip()
            if cpf == "0":
                tela_boas_vindas()
            if validar_cpf(cpf):
                break
            print(Fore.RED + "\n❌ CPF inválido. Deve conter 11 dígitos.\n")

        # Senha
        while True:
            senha = input("Senha: \t\t\t" + Style.RESET_ALL).strip()
            if senha == "0":
                tela_boas_vindas()
            if len(senha) >= 6:
                break
            print(Fore.RED + "\n❌ Senha muito curta. Tente novamente.\n")

        # Confirmação
        while True:
            confirma = input("Confirmar Senha: \t" + Style.RESET_ALL).strip()
            if confirma == "0":
                tela_boas_vindas()
            if senha == confirma:
                break
            print(Fore.RED + "\n❌ As senhas não coincidem. Tente novamente.\n")

        limpar_tela()
        print(Fore.GREEN + f"\n✅ Cadastro realizado com sucesso para {nome}!\n")
        input(Fore.CYAN + "Pressione Enter para continuar...")
        register_user()
        tela_boas_vindas()
        break


def register_user():
    #Registra um novo usuário no banco de dados
    
    db = Database()
    
    
    # Insere o novo usuário
    db.execute("INSERT INTO tb_client (cli_name, cli_email, cli_password, cli_cpf) VALUES (%s, %s, %s, %s)",
            (nome, email, senha, cpf))
   
    
