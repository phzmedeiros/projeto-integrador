# Importa o módulo colorama para colorir o terminal
from colorama import Fore, Style, init

# Importa o módulo os para comandos no sistema operacional
import os

# Importa a variável que contém os dados do usuário logado
from sessao import usuario_logado

# Colorama
init(autoreset=True)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# função principal do menu
def menu():
    while True:
        # limpa a tela a cada volta no loop
        limpar_tela()

        # título
        print(Fore.MAGENTA + Style.BRIGHT + f"""
 __  __ _____ _   _ _   _ 
|  \/  | ____| \ | | \ | |
| |\/| |  _| |  \| |  \| |
| |  | | |___| |\  | |\  |
|_|  |_|_____|_| \_|_| \_|

""")

        
        print(Fore.YELLOW + f"🌿 Bem-vindo, {usuario_logado['nome']}! O que deseja fazer?\n")

         # menu
        print(Fore.CYAN + """
[1] Registrar Consumo do Dia
[2] Ver Relatório do Dia
[3] Ver Histórico
[4] Editar ou Excluir Registro
[5] Perfil
[6] Sair
""")

         
        opcao = input(Fore.GREEN + "→ Escolha uma opção: " + Style.RESET_ALL).strip()

        
        if opcao == "1":
            from registro import registrar_consumo # Importa a função de registrar consumo
            registrar_consumo()
        elif opcao == "2": 
            from relatorio import relatorio_do_dia # Importa a função de gerar relatório do dia
            relatorio_do_dia() 
        elif opcao == "3":
            from historico import ver_historico # Importa a função de ver histórico
            ver_historico()
        elif opcao == "4":
            from editar_excluir import editar_ou_excluir # Importa a função de editar ou excluir registro
            editar_ou_excluir()
        elif opcao == "5":
            from perfil import perfil_usuario
            perfil_usuario(usuario_logado["id"]) # Importa a função de ver perfil do usuário
        
        elif opcao == "6": # sai e volta para a tela de boas-vindas
            from tela_boas_vindas import tela_boas_vindas
            print(Fore.CYAN + "\n👋 Até logo! Retornando à tela inicial...")
            input("Pressione Enter para continuar...")
            tela_boas_vindas()
            break
        else: 
            
            print(Fore.RED + "\n❌ Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...") 
