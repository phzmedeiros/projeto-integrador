from colorama import Fore, Style, init # Importando a biblioteca colorama para formatação de cores
import os # Importando a biblioteca os para limpar a tela
from sessao import usuario_logado # Importando o usuário logado da sessão
init(autoreset=True) # Inicializando a biblioteca colorama para que as cores sejam resetadas automaticamente

# Função para limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir o menu principal
# Esta função é responsável por exibir o menu principal do sistema, onde o usuário pode escolher entre diferentes opções.
def menu():
    # laço infinito para manter o menu ativo
    # enquanto o usuário não escolher a opção de sair
    # e não houver erro de entrada
    while True:
        limpar_tela() # Limpa a tela chamando a função limpar_tela
        # define o título do menu utilizando caracteres ASCII e colorindo com o colorama
        print(Fore.GREEN + Style.BRIGHT + r"""
 _   _       _     _ _   _____                     
| | | |     | |   (_) | |  __ \                    
| |_| | __ _| |__  _| |_| |  \/_ __ ___  ___ _ __  
|  _  |/ _` | '_ \| | __| | __| '__/ _ \/ _ \ '_ \ 
| | | | (_| | |_) | | |_| |_\ \ | |  __/  __/ | | |
\_| |_/\__,_|_.__/|_|\__|\____/_|  \___|\___|_| |_|
""")
        # Exibe o nome do usuário logado
        # utilizando a variável global usuario_logado e colorindo com o colorama
        print(Fore.YELLOW + Style.BRIGHT + f"Bem-vindo, {usuario_logado['nome']}! O que deseja fazer?")
        # define o menu lateral com opções de registro, relatório, histórico, edição/exclusão e perfil
        # e colorindo com o colorama
        print(Fore.CYAN + """
╔═════════════════════════════════════════════════════════════════╗
║                          Menu Principal                         ║
║                                                                 ║
║ [1] Registrar Consumo                                           ║
║ [2] Ver Relatório                                               ║
║ [3] Ver Histórico                                               ║
║ [4] Editar ou Excluir Registro                                  ║
║ [5] Perfil                                                      ║
║ [0] Sair                                                        ║
╚═════════════════════════════════════════════════════════════════╝
""")

        # entrada do usuário para escolher uma opção
        opcao = input(Fore.CYAN + "→ Escolha uma opção: " + Style.RESET_ALL).strip()

        # Verifica a opção escolhida pelo usuário
        # e chama a função correspondente
        if opcao == "1": # se o usuário escolher 1, chama a função de registro
            from registro import registro
            registro()
        elif opcao == "2": # se o usuário escolher 2, chama a função de relatório
            from relatorio import relatorio_do_dia
            relatorio_do_dia()
        elif opcao == "3": # se o usuário escolher 3, chama a função de histórico
            from historico import ver_historico
            ver_historico()
        elif opcao == "4": # se o usuário escolher 4, chama a função de edição/exclusão
            from editar_excluir import editar_ou_excluir
            editar_ou_excluir()
        elif opcao == "5": # se o usuário escolher 5, chama a função de perfil
            from perfil import perfil_usuario
            perfil_usuario(usuario_logado["id"])
        elif opcao == "0": # se o usuário escolher 0, exibe uma mensagem de despedida e encerra o loop
            # Importa a função de tela de boas-vindas
            # para retornar ao menu inicial
            from tela_boas_vindas import tela_boas_vindas
            print(Fore.CYAN + "\nAté logo! Retornando à tela inicial...")
            # espera a ação do usuário pressionar Enter
            input("Pressione Enter para continuar...")
            # chama a função de tela de boas-vindas
            tela_boas_vindas()
            # encerra o loop
            break
        else: # se o usuário digitar uma opção inválida, exibe uma mensagem de erro
            print(Fore.RED + "\nOpção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")