# Importação de bibliotecas padrão do Python e módulos do projeto
import os  # Permite executar comandos do sistema operacional, como limpar a tela do terminal.
import re  # Permite fazer validações com expressões regulares (exemplo: verificar formato de e-mail).
from colorama import init, Fore, Style  # Biblioteca usada para colorir o texto exibido no terminal.

# Importação de módulos do projeto
from banco import Database  # Classe que gerencia a conexão e comandos com o banco de dados.
from criptografia_hills import cifra_hill_criptografar, CHAVE_HILL  # Função e chave da criptografia de senha.

# Inicializa o Colorama, que reseta automaticamente as cores após cada print.
init(autoreset=True)

# Função que limpa a tela do terminal (Windows ou Linux/Mac).
def limpar_tela():
    # Executa o comando 'cls' no Windows e 'clear' em outros sistemas (Linux/Mac).
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que valida se o e-mail digitado segue o padrão nome@dominio.extensão.
def validar_email(email):
    # Utiliza expressão regular para verificar se o e-mail está no formato correto.
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Função que verifica se o CPF possui exatamente 11 números.
def validar_cpf(cpf):
    # Retorna True se o CPF for composto apenas por dígitos e tiver 11 caracteres.
    return cpf.isdigit() and len(cpf) == 11

# Função principal de cadastro de usuário.
def cadastro():
    # Importa a função de boas-vindas para voltar ao menu caso necessário.
    from tela_boas_vindas import tela_boas_vindas

    # Loop principal do cadastro, permite reiniciar o processo caso haja erro ou retorno ao menu.
    while True:
        limpar_tela()  # Limpa a tela antes de exibir a interface.

        # Cabeçalho estilizado com título em ASCII verde.
        titulo_ascii = Fore.GREEN + Style.BRIGHT + r"""
        [Texto ASCII do título do HabitGreen omitido aqui para brevidade...]
        """

        # Instruções para o usuário no menu lateral, em amarelo.
        menu_lateral = Fore.YELLOW + """
┌────────────────────────────────────────────────────────────────────────┐
│ Para se cadastrar ao HabitGreen você deverá inserir seu nome, email,   │
│ CPF e senha, além de ter também que confirmar-la.                      │
│ Caso precise, pressione [0] para voltar ao menu inicial.               │
└────────────────────────────────────────────────────────────────────────┘
"""
        # Exibe o título e o menu lateral na tela.
        print(titulo_ascii + menu_lateral)

        # Coleta do nome do usuário.
        while True:
            nome = input("→ Nome: " + Style.RESET_ALL).strip()  # Solicita o nome e remove espaços extras.
            if nome == "0":  # Se o usuário digitar 0, retorna ao menu inicial.
                tela_boas_vindas()
                return
            else:
                break  # Sai do loop se o nome for válido.

        # Coleta e validação do e-mail.
        while True:
            email = input("→ E-mail: " + Style.RESET_ALL).strip()  # Solicita o e-mail.
            if email == "0":
                tela_boas_vindas()
                return
            if not validar_email(email):  # Verifica se o formato do e-mail é válido.
                print(Fore.RED + "\nE-mail inválido. Tente novamente.\n")
                continue  # Solicita novamente se o e-mail for inválido.
            db = Database()  # Cria uma conexão com o banco de dados.
            ja_existe_email = db.fetchone("SELECT * FROM tb_client WHERE cli_email = %s", (email,))
            db.close()  # Fecha a conexão.
            if ja_existe_email:  # Verifica se o e-mail já está cadastrado.
                print(Fore.RED + "\nE-mail já cadastrado. Tente outro.\n")
                continue
            break  # Sai do loop se o e-mail for válido e não estiver cadastrado.

        # Coleta e validação do CPF.
        while True:
            cpf = input("→ CPF: " + Style.RESET_ALL).strip()  # Solicita o CPF.
            if cpf == "0":
                tela_boas_vindas()
                return
            if not validar_cpf(cpf):  # Verifica se é numérico e tem 11 dígitos.
                print(Fore.RED + "\nCPF inválido. Deve conter 11 dígitos.\n")
                continue
            db = Database()  # Cria uma conexão com o banco de dados.
            ja_existe_cpf = db.fetchone("SELECT * FROM tb_client WHERE cli_cpf = %s", (cpf,))
            db.close()  # Fecha a conexão.
            if ja_existe_cpf:  # Verifica duplicidade de CPF no banco.
                print(Fore.RED + "\nCPF já cadastrado. Tente outro.\n")
                continue
            break  # Sai do loop se o CPF for válido e não estiver cadastrado.

        # Coleta e validação da senha.
        while True:
            senha = input("→ Senha: " + Style.RESET_ALL).strip()  # Solicita a senha.
            if senha == "0":
                tela_boas_vindas()
                return
            if len(senha) >= 6:  # A senha deve ter no mínimo 6 caracteres.
                break
            print(Fore.RED + "\nSenha muito curta. Tente novamente.\n")

        # Confirmação da senha.
        while True:
            confirma = input("→ Confirmar Senha: " + Style.RESET_ALL).strip()  # Solicita confirmação da senha.
            if confirma == "0":
                tela_boas_vindas()
                return
            if senha == confirma:  # Verifica se as senhas coincidem.
                break
            print(Fore.RED + "\nAs senhas não coincidem. Tente novamente.\n")

        limpar_tela()  # Limpa tela antes de finalizar o processo.

        # Chama a função para registrar o usuário no banco.
        register_user(nome, email, senha, cpf)

        # Após cadastro, volta à tela inicial.
        tela_boas_vindas()
        break  # Encerra o loop principal do cadastro.

# Função que realiza o salvamento do usuário no banco de dados.
def register_user(nome, email, senha, cpf):
    # Criptografa a senha usando a Cifra de Hill antes de armazenar.
    senha_criptografada = cifra_hill_criptografar(senha, CHAVE_HILL)

    db = Database()  # Cria uma conexão com o banco de dados.
    # Executa o comando SQL para inserir os dados no banco.
    db.execute("INSERT INTO tb_client (cli_name, cli_email, cli_password, cli_cpf) VALUES (%s, %s, %s, %s)",
               (nome, email, senha_criptografada, cpf))

    # Exibe mensagem de sucesso com o nome do usuário.
    print(Fore.GREEN + f"\nCadastro realizado com sucesso para {nome}!\n")
    # Aguarda o usuário pressionar Enter para continuar.
    input(Fore.CYAN + "Pressione [Enter] para continuar...")
