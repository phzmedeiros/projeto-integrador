# Importa a classe Database do módulo banco, responsável pela conexão e operações com o banco de dados MySQL.
from banco import Database

# Importa constantes e funções da biblioteca colorama para colorir textos no terminal.
from colorama import Fore, Style, init

# Importa o dicionário usuario_logado do módulo sessao, que armazena informações do usuário autenticado.
from sessao import usuario_logado

# Importa a função de descriptografia e a chave da cifra de Hill, usada para proteger senhas.
from criptografia_hills import cifra_hill_descriptografar, CHAVE_HILL

# Importa o módulo os, utilizado para executar comandos do sistema operacional (como limpar a tela).
import os

# Inicializa o colorama para que as cores sejam resetadas automaticamente após cada print.
init(autoreset=True)

# Função para limpar a tela do terminal, tornando a interface mais amigável.
def limpar_tela():
    # Se o sistema operacional for Windows, executa 'cls', senão executa 'clear' (Linux/Mac).
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal de login do sistema.
def login():
    limpar_tela()  # Limpa a tela antes de exibir a interface de login.

    # Título em ASCII estilizado, exibido em verde e negrito.
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
    # Menu lateral com instruções para o usuário, exibido em amarelo.
    menu_lateral = Fore.YELLOW + """
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Faça seu login para acessar o HabitGreen                                               │
│ Digite suas credenciais (email e senha) ou pressione [0] para voltar ao menu inicial   │
└────────────────────────────────────────────────────────────────────────────────────────┘
"""
    # Exibe o título e o menu lateral na tela.
    print(titulo_ascii + menu_lateral)

    # Loop principal do login, permite tentativas até sucesso ou retorno ao menu.
    while True:
        # Importação local para evitar importação circular.
        from tela_boas_vindas import tela_boas_vindas

        # Solicita o e-mail do usuário.
        email = input(Fore.CYAN + "→ E-mail: " + Style.RESET_ALL).strip()
        if email == "0":  # Se o usuário digitar 0, retorna ao menu inicial.
            tela_boas_vindas()
            return
        
        # Solicita a senha do usuário.
        senha = input(Fore.CYAN + "→ Senha: " + Style.RESET_ALL).strip()
        if senha == "0":  # Se o usuário digitar 0, retorna ao menu inicial.
            tela_boas_vindas()
            return

        # Chama a função de verificação de login.
        if check_login(email, senha):
            # Importação local do menu para evitar importação circular.
            from menu import menu
            limpar_tela()  # Limpa a tela antes de exibir mensagem de sucesso.
            print(Fore.GREEN + Style.BRIGHT + "\nLogin realizado com sucesso!")
            limpar_tela()  # Limpa novamente antes de exibir o menu principal.
            menu()         # Redireciona o usuário para o menu principal do sistema.
            break          # Sai do loop de login.
        else:
            # Se o login falhar, exibe mensagem de erro em vermelho.
            print(Fore.RED + Style.BRIGHT + "\nE-mail ou senha inválidos. Tente novamente.\n")

# Função que verifica as credenciais do usuário.
# Parâmetros:
#   email: e-mail digitado pelo usuário.
#   senha: senha digitada pelo usuário.
def check_login(email, senha):
    db = Database()  # Cria uma conexão com o banco de dados.

    # Consulta o usuário pelo e-mail informado.
    user = db.fetchone("SELECT * FROM tb_client WHERE cli_email = %s", (email,))
    db.close()  # Fecha a conexão com o banco.

    # Verifica se o e-mail está cadastrado no sistema.
    if user is None:
        return False  # Nenhum usuário encontrado com esse e-mail.

    # Recupera a senha criptografada do banco (posição 3 da tabela).
    senha_criptografada = user[3]

    # Descriptografa a senha com a Cifra de Hill.
    senha_descriptografada = cifra_hill_descriptografar(senha_criptografada, CHAVE_HILL)

    # Remove qualquer caractere de padding (🐻) usado na criptografia.
    senha_descriptografada = senha_descriptografada.replace("🐻", "")

    # Compara a senha digitada com a senha real (descriptografada).
    if senha == senha_descriptografada:
        # Armazena as informações do usuário logado na sessão.
        usuario_logado["id"] = user[0]      # ID do usuário.
        usuario_logado["nome"] = user[1]    # Nome do usuário.
        usuario_logado["email"] = user[2]   # E-mail do usuário.
        return True  # Login bem-sucedido.

    # Senha incorreta.
    return False