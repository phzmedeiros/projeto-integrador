import os
import re
from colorama import init, Fore, Style

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


        # E-mail
        while True:
            email = input(Fore.YELLOW + "-> E-mail: " + Style.RESET_ALL).strip()
            if email == "0":
                return
            if validar_email(email):
                break
            print(Fore.RED + "❌ E-mail inválido. Tente novamente.\n")

        # CPF
        while True:
            cpf = input(Fore.YELLOW + "-> CPF (somente números): " + Style.RESET_ALL).strip()
            if cpf == "0":
                return
            if validar_cpf(cpf):
                break
            print(Fore.RED + "❌ CPF inválido. Deve conter 11 dígitos.\n")

        # Senha
        while True:
            senha = input(Fore.YELLOW + "-> Senha (mínimo 6 caracteres): " + Style.RESET_ALL).strip()
            if senha == "0":
                return
            if len(senha) >= 6:
                break
            print(Fore.RED + "❌ Senha muito curta. Tente novamente.\n")

        # Confirmação
        while True:
            confirma = input(Fore.YELLOW + "-> Confirmar Senha: " + Style.RESET_ALL).strip()
            if confirma == "0":
                return
            if senha == confirma:
                break
            print(Fore.RED + "❌ As senhas não coincidem. Tente novamente.\n")

        limpar_tela()
        print(Fore.GREEN + f"\n✅ Cadastro realizado com sucesso para {email}!\n")
        input(Fore.CYAN + "Pressione Enter para continuar...")
        break