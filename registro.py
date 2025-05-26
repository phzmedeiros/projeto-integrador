# Importa o módulo 'os', utilizado para executar comandos do sistema operacional, como limpar a tela do terminal.
import os

# Importa a classe 'datetime' do módulo 'datetime', usada para manipulação de datas e horas.
from datetime import datetime

# Importa funções e constantes da biblioteca colorama para colorir textos no terminal.
from colorama import Fore, Style, init

# Importa a classe Database do módulo banco, responsável pela conexão e operações com o banco de dados.
from banco import Database

# Importa o dicionário usuario_logado do módulo sessao, que armazena informações do usuário autenticado.
from sessao import usuario_logado

# Inicializa o colorama para que as cores sejam resetadas automaticamente após cada print.
init(autoreset=True)

# Função para limpar a tela do terminal, tornando a interface mais amigável.
def limpar_tela():
    # Se o sistema operacional for Windows, executa 'cls', senão executa 'clear' (Linux/Mac).
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal para registrar o consumo diário do usuário.
# Parâmetros opcionais: dia, mes, ano (permite registrar para datas específicas, se necessário).
def registro(dia=None, mes=None, ano=None):
    limpar_tela()  # Limpa a tela antes de exibir a interface de registro.

    # Título em ASCII estilizado, exibido em verde e negrito, com instruções ao lado.
    titulo_ascii = Fore.GREEN + Style.BRIGHT + r"""
______ _____ _____ _____ _____ ___________ _____  ______ _____   │
| ___ \  ___|  __ \_   _/  ___|_   _| ___ \  _  | |  _  \  ___|  │
| |_/ / |__ | |  \/ | | \ `--.  | | | |_/ / | | | | | | | |__    │  ┌────────────────────────────────────────────────┐
|    /|  __|| | __  | |  `--. \ | | |    /| | | | | | | |  __|   │  │ Registre e acompanhe seu consumo diário de     │
| |\ \| |___| |_\ \_| |_/\__/ / | | | |\ \| \_/ | | |/ /| |___   │  │               recursos naturais.               │
\_| \_\____/ \____/\___/\____/  \_/ \_| \_|\___/  |___/ \____/   │  │   Fornecendo essas informações, é possível     │
 _____ _____ _   _ _____ _   ____  ________                      │  │  analisar hábitos e identificar maneiras de    │
/  __ \  _  | \ | /  ___| | | |  \/  |  _  |                     │  │         reduzir o impacto ambiental.           │
| /  \/ | | |  \| \ `--.| | | | .  . | | | |                     │  └────────────────────────────────────────────────┘
| |   | | | | . ` |`--. \ | | | |\/| | | | |                     │
| \__/\ \_/ / |\  /\__/ / |_| | |  | \ \_/ /                     │
 \____/\___/\_| \_|____/ \___/\_|  |_/\___/                      │
"""
    print(titulo_ascii)

    # Exibe instruções para o usuário escolher o tipo de registro (hoje ou outro dia).
    print(Fore.YELLOW + Style.BRIGHT + "Escolha o tipo de registro:")
    hoje = datetime.now()  # Obtém a data e hora atuais.
    print(Fore.CYAN + f"""
╔═════════════════════════════════════════════════════════════════╗
║                        Tipo de Registro                         ║
╠═════════════════════════════════════════════════════════════════╣
║ [1] Registrar o dia de hoje     ({hoje.strftime('%d/%m/%Y')})                    ║
║ [2] Escolher outro dia                                          ║
║ [0] Voltar ao menu                                              ║
╚═════════════════════════════════════════════════════════════════╝
""")

    # Loop para garantir que o usuário escolha uma opção válida para o tipo de registro.
    while True:
        escolha = input(Fore.WHITE + Style.BRIGHT + "→ Escolha uma opção: ").strip()
        if escolha == "1":
            data_registro = hoje.date()  # Usa a data de hoje.
            break
        elif escolha == "2":
            # Permite ao usuário digitar uma data específica.
            while True:
                data_str = input("Digite a data (dd/mm/aaaa): ").strip()
                try:
                    data_registro = datetime.strptime(data_str, "%d/%m/%Y").date()
                    break
                except ValueError:
                    print(Fore.RED + "Data inválida. Tente novamente.")
            break
        elif escolha == "0":
            # Importação local para evitar importação circular.
            from menu import menu
            menu()  # Retorna ao menu principal.
            return
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

    limpar_tela()
    print(Fore.YELLOW + f"\nRegistro do dia {data_registro.strftime('%d/%m/%Y')}\n")

    # Entrada de dados do consumo de água, com validação para garantir valor positivo.
    while True:
        try:
            agua = float(input("→ Consumo de água (litros): ").strip())
            if agua < 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número positivo para a água.")

    # Entrada de dados do consumo de energia elétrica, com validação.
    while True:
        try:
            energia = float(input("→ Consumo de energia elétrica (kWh): ").strip())
            if energia < 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número positivo para a energia.")

    # Entrada de dados do lixo orgânico, com validação.
    while True:
        try:
            lixo_organico = float(input("→ Quantidade de lixo orgânico (kg): ").strip())
            if lixo_organico < 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número positivo para o lixo orgânico.")

    # Entrada de dados do lixo reciclável, com validação.
    while True:
        try:
            lixo_reciclavel = float(input("→ Quantidade de lixo reciclável (kg): ").strip())
            if lixo_reciclavel < 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número positivo para o lixo reciclável.")

    # Exibe as categorias de transporte disponíveis, com exemplos, em formato de tabela.
    print(Fore.YELLOW + """
╔════════════════════════════════════════════════════════════════╗
║          Categoria de Transporte Utilizado no Dia              ║
╠═════════════════╦══════════════════════════════════════════════╣
║ [1] Sustentável ║ A pé, bicicleta, skate, patinete elétrico    ║
║ [2] Misto       ║ Carro elétrico, transporte público, carona   ║
║ [3] Poluente    ║ Moto, carro a combustão, avião               ║
╚═════════════════╩══════════════════════════════════════════════╝
""")

    # Dicionário que mapeia a escolha do usuário para o texto correspondente da categoria.
    mapa_categorias = {
        "1": "sustentável",
        "2": "misto",
        "3": "poluente"
    }

    # Loop para garantir que o usuário escolha uma categoria de transporte válida.
    while True:
        tipo_transporte = input("→ Escolha a categoria (1/2/3): ").strip()
        if tipo_transporte in mapa_categorias:
            transporte = mapa_categorias[tipo_transporte]
            break
        else:
            print(Fore.RED + "Opção inválida. Digite 1, 2 ou 3.")

    # Cria uma conexão com o banco de dados.
    db = Database()
    # Executa o comando SQL para inserir o registro no banco.
    db.execute("""
        INSERT INTO tb_register (user_id, date, water, energy, organic_waste, recyclable_waste, transport)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (usuario_logado["id"], data_registro, agua, energia, lixo_organico, lixo_reciclavel, transporte))
    db.close()  # Fecha a conexão com o banco.

    # Exibe mensagem de sucesso ao usuário, confirmando o registro.
    print(Fore.GREEN + f"\nRegistro do dia {data_registro.strftime('%d/%m/%Y')} salvo com sucesso!")
    input(Fore.YELLOW + "Pressione Enter para continuar...")  # Aguarda o usuário antes de retornar.
