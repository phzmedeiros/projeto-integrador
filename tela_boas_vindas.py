# Importa o módulo 'os', utilizado para executar comandos do sistema operacional, como limpar a tela do terminal.
import os

# Importa funções e constantes da biblioteca colorama para colorir textos no terminal.
from colorama import Fore, Style, init

# Importa a função 'login' do módulo login, responsável pelo fluxo de autenticação do usuário.
from login import login

# Importa a função 'cadastro' do módulo cadastro, responsável pelo fluxo de cadastro de novos usuários.
from cadastro import cadastro

# Inicializa o colorama para que as cores sejam resetadas automaticamente após cada print.
init(autoreset=True) 

# Função para limpar a tela do terminal, tornando a interface mais amigável.
def limpar_tela():
    # Se o sistema operacional for Windows, executa 'cls', senão executa 'clear' (Linux/Mac).
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal que exibe a tela de boas-vindas do sistema.
# Esta função apresenta o título, informações do projeto, opções iniciais e direciona o usuário conforme a escolha.
def tela_boas_vindas():
    limpar_tela()  # Limpa a tela antes de exibir a interface.

    # Define o título do sistema com arte ASCII, estilizado em verde e negrito.
    # Inclui também informações sobre o propósito do sistema e os desenvolvedores.
    titulo_ascii = Fore.GREEN + Style.BRIGHT + r"""                                                                                            
______                      _   _  _             _                             │
| ___ \                    | | | |(_)           | |                            │      Aplicação para desenvolvimento sustentável.
| |_/ /  ___    __ _  ___  | | | | _  _ __    __| |  __ _  ___                 │      Análise de dados e mentoria pra uma melhor
| ___ \ / _ \  / _` |/ __| | | | || || '_ \  / _` | / _` |/ __|                │      sustentabilidade e uma melhor rotina pessoal.
| |_/ /| (_) || (_| |\__ \ \ \_/ /| || | | || (_| || (_| |\__ \                │ 
\____/  \___/  \__,_||___/  \___/ |_||_| |_| \__,_| \__,_||___/                │      Desenvolvido por:
                _   _         _      _  _    _____                             │      Alinne Monteiro de Melo
               | | | |       | |    (_)| |  |  __ \                            │      Alycia Santos Bond
  __ _   ___   | |_| |  __ _ | |__   _ | |_ | |  \/ _ __  ___   ___  _ __      │      Pedro Henrique Medeiros dos Reis
 / _` | / _ \  |  _  | / _` || '_ \ | || __|| | __ | '__|/ _ \ / _ \| '_ \     │      Rafael Antônio Candian 
| (_| || (_) | | | | || (_| || |_) || || |_ | |_\ \| |  |  __/|  __/| | | |    │
 \__,_| \___/  \_| |_/ \__,_||_.__/ |_| \__| \____/|_|   \___| \___||_| |_|    │      Pontifícia Universidade Católica de Campinas
                                                                               │
"""

    # Define o menu lateral com instruções para o usuário, usando cor amarela.
    menu_lateral = Fore.YELLOW + r"""
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Para acessar ao sistema, selecione abaixo uma das opções disponíveis.  │
 │ Com as próximas telas a interação é a mesma, fique livre e bom uso!    │
 └────────────────────────────────────────────────────────────────────────┘
"""

    # Define as opções iniciais do sistema, apresentadas em azul claro e negrito.
    opcoes = Fore.CYAN + Style.BRIGHT + r"""
┌───────────────┐
│ Opções:       │
│               │
│ [1] Login     │
│ [2] Cadastrar │
│ [0] Sair      │
└───────────────┘
"""

    # Exibe o título, o menu lateral e as opções na tela.
    print(titulo_ascii + menu_lateral + opcoes)

    # Loop para garantir que o usuário escolha uma opção válida.
    while True:  # Mantém o usuário na tela até que uma opção válida seja escolhida.
        opcao = input(Fore.WHITE + Style.BRIGHT + "Digite a opção escolhida: ")
        if opcao == "1":
            # Se o usuário escolher "1", inicia o fluxo de login.
            login()
            break  # Sai do loop após o login.
        elif opcao == "2":
            # Se o usuário escolher "2", inicia o fluxo de cadastro.
            cadastro()
            break  # Sai do loop após o cadastro.
        elif opcao == "0":
            # Se o usuário escolher "0", exibe mensagem de despedida e encerra o programa.
            print(Fore.GREEN + "Até logo!")
            break
        else:
            # Se a opção for inválida, exibe mensagem de erro em vermelho e repete o loop.
            print(Fore.RED + "Opção inválida. Tente novamente.")

# Fim do arquivo: este módulo implementa a tela inicial do sistema, centralizando a navegação para login, cadastro ou saída.
# O uso de cores, arte ASCII e validação de entrada torna a experiência do usuário mais amigável e profissional.
# Importações locais e funções bem definidas facilitam a manutenção e a expansão do sistema.