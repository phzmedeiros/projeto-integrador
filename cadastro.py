import os
import re
from colorama import init, Fore, Style

init(autoreset=True)  # Iniciar colorama

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funções de validação de e-mail e CPF
def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Função de cadastro
def cadastro():
    while True:
        limpar_tela()
        print(Fore.CYAN + Style.BRIGHT + """
   ____      _        _                 
  / ___|__ _| | _____| |__   __ _ _ __  
 | |   / _` | |/ / _ \ '_ \ / _` | '_ \ 
 | |__| (_| |   <  __/ |_) | (_| | | | |
  \____\__,_|_|\_\___|_.__/ \__,_|_| |_|

""" + Fore.YELLOW + "[CADASTRO DE NOVO USUÁRIO]" + Style.RESET_ALL)
        print(Fore.MAGENTA + "(Digite 0 a qualquer momento para voltar)\n")

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