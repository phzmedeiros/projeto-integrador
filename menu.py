from colorama import Fore, Style, init
import os
from sessao import usuario_logado
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        limpar_tela()
        print(Fore.GREEN + Style.BRIGHT + r"""
 _   _       _     _ _   _____                     
| | | |     | |   (_) | |  __ \                    
| |_| | __ _| |__  _| |_| |  \/_ __ ___  ___ _ __  
|  _  |/ _` | '_ \| | __| | __| '__/ _ \/ _ \ '_ \ 
| | | | (_| | |_) | | |_| |_\ \ | |  __/  __/ | | |
\_| |_/\__,_|_.__/|_|\__|\____/_|  \___|\___|_| |_|
""")
        print(Fore.YELLOW + Style.BRIGHT + f"Bem-vindo, {usuario_logado['nome']}! O que deseja fazer?")

        print(Fore.YELLOW + """
[1] Registrar Consumo
[2] Ver Relatório
[3] Ver Histórico
[4] Editar ou Excluir Registro
[5] Perfil
[0] Sair
""")

        opcao = input(Fore.CYAN + "→ Escolha uma opção: " + Style.RESET_ALL).strip()

        if opcao == "1":
            from registro import registro
            registro()
        elif opcao == "2":
            from relatorio import relatorio_do_dia
            relatorio_do_dia()
        # elif opcao == "3":
        #     from historico import ver_historico
        #     ver_historico()
        # elif opcao == "4":
        #     #from editar_excluir import editar_ou_excluir
        #     #editar_ou_excluir()
        # elif opcao == "5":
        #     #from perfil import perfil_usuario
        #     #perfil_usuario(usuario_logado["id"])
        elif opcao == "0":
            from tela_boas_vindas import tela_boas_vindas
            print(Fore.CYAN + "\nAté logo! Retornando à tela inicial...")
            input("Pressione Enter para continuar...")
            tela_boas_vindas()
            break
        else:
            print(Fore.RED + "\nOpção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
