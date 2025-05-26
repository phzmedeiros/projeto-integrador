# Importa funções e constantes da biblioteca colorama para colorir textos no terminal.
from colorama import Fore, Style, init

# Importa o módulo os, utilizado para executar comandos do sistema operacional (como limpar a tela).
import os

# Importa o dicionário usuario_logado do módulo sessao, que armazena informações do usuário autenticado.
from sessao import usuario_logado

# Inicializa o colorama para que as cores sejam resetadas automaticamente após cada print.
init(autoreset=True)

# Função para limpar a tela do terminal, tornando a interface mais amigável.
def limpar_tela():
    # Se o sistema operacional for Windows, executa 'cls', senão executa 'clear' (Linux/Mac).
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal do menu do sistema.
# Exibe as opções disponíveis para o usuário e direciona para a funcionalidade escolhida.
def menu():
    while True:  # Loop principal do menu, mantém o usuário no menu até que ele escolha sair.
        limpar_tela()  # Limpa a tela a cada iteração para melhor visualização.

        # Exibe o título do sistema em ASCII, estilizado em verde e negrito.
        print(Fore.GREEN + Style.BRIGHT + r"""
 _   _       _     _ _   _____                     
| | | |     | |   (_) | |  __ \                    
| |_| | __ _| |__  _| |_| |  \/_ __ ___  ___ _ __  
|  _  |/ _` | '_ \| | __| | __| '__/ _ \/ _ \ '_ \ 
| | | | (_| | |_) | | |_| |_\ \ | |  __/  __/ | | |
\_| |_/\__,_|_.__/|_|\__|\____/_|  \___|\___|_| |_|
""")

        # Exibe mensagem de boas-vindas personalizada com o nome do usuário logado, em amarelo e negrito.
        print(Fore.YELLOW + Style.BRIGHT + f"Bem-vindo, {usuario_logado['nome']}! O que deseja fazer?")

        # Exibe o menu principal com as opções disponíveis, usando arte de caixa para melhor visualização.
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

        # Solicita ao usuário que escolha uma opção do menu.
        opcao = input(Fore.CYAN + "→ Escolha uma opção: " + Style.RESET_ALL).strip()

        # Bloco de controle de fluxo para direcionar o usuário conforme a opção escolhida.
        if opcao == "1":
            # Importação local para evitar importação circular.
            from registro import registro
            registro()  # Chama a função para registrar consumo.
        elif opcao == "2":
            # Importação local para evitar importação circular.
            from relatorio import relatorio_do_dia
            relatorio_do_dia()  # Chama a função para exibir o relatório do dia.
        elif opcao == "3":
            # Importação local para evitar importação circular.
            from historico import ver_historico
            ver_historico()  # Chama a função para visualizar o histórico de registros.
        elif opcao == "4":
            # Importação local para evitar importação circular.
            from editar_excluir import editar_ou_excluir
            editar_ou_excluir()  # Chama a função para editar ou excluir um registro.
        elif opcao == "5":
            # Importação local para evitar importação circular.
            from perfil import perfil_usuario
            perfil_usuario(usuario_logado["id"])  # Chama a função para exibir o perfil do usuário logado.
        elif opcao == "0":
            # Importação local para evitar importação circular.
            from tela_boas_vindas import tela_boas_vindas
            # Exibe mensagem de despedida e retorna à tela inicial.
            print(Fore.CYAN + "\nAté logo! Retornando à tela inicial...")
            input("Pressione Enter para continuar...")
            tela_boas_vindas()
            break  # Sai do loop do menu, encerrando a função.
        else:
            # Se a opção for inválida, informa o erro e solicita nova entrada.
            print(Fore.RED + "\nOpção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

# Fim do arquivo: este módulo implementa o menu principal do sistema, centralizando a navegação entre as principais funcionalidades.
# O uso de cores, arte ASCII e validação de entrada torna a experiência do usuário mais amigável e segura.
# Importações locais são utilizadas para evitar problemas de importação circular entre módulos do projeto.
