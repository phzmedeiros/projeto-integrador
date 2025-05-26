# Importa a biblioteca 'os' para executar comandos do sistema operacional, como limpar a tela do terminal.
import os

# Importa a classe 'datetime' do módulo 'datetime' para manipulação de datas.
from datetime import datetime

# Importa funções e constantes da biblioteca 'colorama' para colorir textos no terminal.
from colorama import Fore, Style, init

# Importa a classe 'Database' do módulo 'banco', responsável pela conexão e operações com o banco de dados.
from banco import Database

# Importa o dicionário 'usuario_logado' do módulo 'sessao', que armazena informações do usuário atualmente autenticado.
from sessao import usuario_logado

# Inicializa o colorama para que as cores sejam resetadas automaticamente após cada print.
init(autoreset=True) # Boa prática para evitar que as cores "vazem" para outros textos.

# Função para limpar a tela do terminal, tornando a interface mais amigável.
def limpar_tela():
    # Se o sistema operacional for Windows, executa 'cls', senão executa 'clear' (Linux/Mac).
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que retorna um texto ASCII estilizado para ser usado como título nas telas de edição/exclusão.
def titulo_ascii():
    # Retorna uma string com arte ASCII, usando cor amarela e estilo negrito.
    return Fore.YELLOW + Style.BRIGHT + r"""
 _____    _ _ _              ______          _           
|  ___|  | (_) |             |  _  \        | |          
| |__  __| |_| |_ __ _ _ __  | | | |__ _  __| | ___  ___ 
|  __|/ _` | | __/ _` | '__| | | | / _` |/ _` |/ _ \/ __|
| |__| (_| | | || (_| | |    | |/ / (_| | (_| | (_) \__ \
\____/\__,_|_|\__\__,_|_|    |___/ \__,_|\__,_|\___/|___/
"""

# Função responsável por editar um registro de consumo diário.
# Parâmetro:
#   data: objeto datetime.date representando a data do registro a ser editado.
def editar_registro(data):
    limpar_tela()  # Limpa a tela para melhor visualização.
    print(titulo_ascii())  # Exibe o título estilizado.
    # Exibe mensagem informando a data do registro que será editado.
    print(Fore.YELLOW + f"\nEdição de Registro do dia {data.strftime('%d/%m/%Y')}\n")

    # Cria uma instância do banco de dados para acessar os dados.
    db = Database()
    # Busca o registro do usuário logado para a data informada.
    registro = db.fetchone(
        "SELECT id, water, energy, organic_waste, recyclable_waste, transport FROM tb_register WHERE user_id = %s AND date = %s",
        (usuario_logado["id"], data)
    )

    # Se não encontrar o registro, informa o usuário e retorna.
    if not registro:
        print(Fore.RED + "Registro não encontrado.")
        db.close()  # Fecha a conexão com o banco.
        input("Pressione Enter para voltar...")
        return

    # Desempacota os valores do registro retornado do banco.
    reg_id, water, energy, lixo_org, lixo_rec, transporte = registro

    # Função interna para solicitar ao usuário um novo valor para um campo numérico.
    # Parâmetros:
    #   label: texto descritivo do campo.
    #   atual: valor atual do campo.
    #   tipo: tipo de dado esperado (float por padrão).
    def novo_valor(label, atual, tipo=float):
        while True:
            # Solicita ao usuário o novo valor, mostrando o valor atual.
            val = input(f"{label} atual: {atual} → Novo valor (ou Enter para manter): ").strip()
            # Se o usuário pressionar Enter, mantém o valor atual.
            if val == "":
                return atual
            try:
                # Tenta converter o valor para o tipo esperado (float ou int).
                return tipo(val)
            except:
                # Se a conversão falhar, informa o erro e repete a solicitação.
                print(Fore.RED + "Valor inválido. Tente novamente.")

    # Função interna para editar o tipo de transporte utilizado.
    # Parâmetro:
    #   atual: valor atual do campo transporte.
    def novo_transporte(atual):
        # Exibe as opções de transporte disponíveis.
        print(Fore.YELLOW + "\nTipo de Transporte:")
        print(Fore.YELLOW + """
╔════════════════════════════════════════════════════════════════╗
║          Categoria de Transporte Utilizado no Dia              ║
╠═════════════════╦══════════════════════════════════════════════╣
║ [1] Sustentável ║ A pé, bicicleta, skate, patinete elétrico    ║
║ [2] Misto       ║ Carro elétrico, transporte público, carona   ║
║ [3] Poluente    ║ Moto, carro a combustão, avião               ║
╚═════════════════╩══════════════════════════════════════════════╝
""")
        # Solicita ao usuário a escolha do novo tipo de transporte.
        escolha = input("Novo tipo (ou Enter para manter): ").strip()
        # Retorna o valor correspondente à escolha do usuário.
        if escolha == "1": return "sustentável"
        elif escolha == "2": return "misto"
        elif escolha == "3": return "poluente"
        else: return atual  # Se pressionar Enter, mantém o valor atual.

    # Solicita ao usuário os novos valores para cada campo do registro.
    water = novo_valor("→ Água (L)", water)
    energy = novo_valor("→ Energia (kWh)", energy)
    lixo_org = novo_valor("→ Lixo Orgânico (kg)", lixo_org)
    lixo_rec = novo_valor("→ Lixo Reciclável (kg)", lixo_rec)
    transporte = novo_transporte(transporte)

    # Atualiza o registro no banco de dados com os novos valores informados.
    db.execute("""
        UPDATE tb_register
        SET water = %s, energy = %s, organic_waste = %s, recyclable_waste = %s, transport = %s
        WHERE id = %s
    """, (water, energy, lixo_org, lixo_rec, transporte, reg_id))
    db.close()  # Fecha a conexão com o banco.

    # Informa ao usuário que o registro foi atualizado com sucesso.
    print(Fore.GREEN + "\n✅ Registro atualizado com sucesso!")
    input("Pressione Enter para voltar...")

# Função responsável por excluir um registro de consumo diário.
# Parâmetro:
#   data: objeto datetime.date representando a data do registro a ser excluído.
def excluir_registro(data):
    limpar_tela()  # Limpa a tela para melhor visualização.
    print(titulo_ascii())  # Exibe o título estilizado.
    # Exibe mensagem informando a data do registro que será excluído.
    print(Fore.YELLOW + f"\nExclusão de Registro do dia {data.strftime('%d/%m/%Y')}\n")

    db = Database()  # Cria uma instância do banco de dados.
    # Busca o registro do usuário logado para a data informada.
    registro = db.fetchone(
        "SELECT id FROM tb_register WHERE user_id = %s AND date = %s",
        (usuario_logado["id"], data)
    )

    # Se não encontrar o registro, informa o usuário e retorna.
    if not registro:
        print(Fore.RED + "Registro não encontrado.")
        db.close()  # Fecha a conexão com o banco.
        input("Pressione Enter para voltar...")
        return

    # Obtém o ID do registro a ser excluído.
    reg_id = registro[0]
    # Solicita confirmação do usuário antes de excluir o registro.
    confirm = input(Fore.RED + "Tem certeza que deseja excluir este registro? (s/n): ").strip().lower()
    if confirm == "s":
        # Se confirmado, executa o comando SQL para excluir o registro.
        db.execute("DELETE FROM tb_register WHERE id = %s", (reg_id,))
        print(Fore.GREEN + "\n✅ Registro excluído com sucesso!")
    else:
        # Se não confirmado, informa que a operação foi cancelada.
        print(Fore.YELLOW + "\nOperação cancelada.")
    db.close()  # Fecha a conexão com o banco.
    input("Pressione Enter para voltar...")

# Função principal que permite ao usuário escolher editar ou excluir um registro.
def editar_ou_excluir():
    limpar_tela()  # Limpa a tela para melhor visualização.
    print(titulo_ascii())  # Exibe o título estilizado.
    # Exibe instrução para o usuário escolher a data do registro.
    print(Fore.YELLOW + "\nEscolha a data do registro que deseja alterar ou excluir:\n")

    # Loop para garantir que o usuário informe uma data válida ou opte por voltar.
    while True:
        # Solicita a data no formato dd/mm/aaaa ou [0] para voltar.
        data_str = input("Digite a data (dd/mm/aaaa) ou [0] para voltar: ").strip()
        if data_str == "0":
            return  # Retorna ao menu anterior se o usuário digitar 0.
        try:
            # Tenta converter a string informada em um objeto de data.
            data = datetime.strptime(data_str, "%d/%m/%Y").date()
            break  # Sai do loop se a data for válida.
        except ValueError:
            # Se a data for inválida, informa o erro e repete a solicitação.
            print(Fore.RED + "❌ Data inválida. Tente novamente.")

    # Exibe opções para o usuário escolher o que deseja fazer com o registro.
    print(Fore.YELLOW + "\nO que deseja fazer com esse registro?\n")
    print(Fore.YELLOW + "[1] Editar")
    print(Fore.YELLOW + "[2] Excluir")
    print(Fore.YELLOW + "[0] Cancelar")
    opcao = input("→ Escolha: ").strip()

    # Verifica a opção escolhida pelo usuário e executa a ação correspondente.
    if opcao == "1":
        editar_registro(data)  # Chama a função para editar o registro.
    elif opcao == "2":
        excluir_registro(data)  # Chama a função para excluir o registro.
    elif opcao == "0":
        return  # Retorna ao menu anterior.
    else:
        # Se a opção for inválida, informa o erro.
        print(Fore.RED + "Opção inválida.")

# Fim do arquivo. Todas as funções acima permitem ao usuário editar ou excluir registros de consumo diário,
# como água, energia, lixo e transporte, de maneira interativa e segura.
# O código utiliza cores para facilitar a visualização e pede confirmação antes de excluir dados.
# Ele também valida entradas do usuário para evitar erros e garante que apenas registros existentes possam ser alterados.
# O objetivo é tornar o processo de edição e exclusão de registros simples, claro e acessível mesmo para quem não tem experiência em programação.
