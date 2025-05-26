import os
from datetime import datetime
from colorama import Fore, Style, init
from banco import Database
from sessao import usuario_logado

init(autoreset=True) # Iniciar colorama

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo_ascii():
    return Fore.YELLOW + Style.BRIGHT + r"""
 _____    _ _ _              ______          _           
|  ___|  | (_) |             |  _  \        | |          
| |__  __| |_| |_ __ _ _ __  | | | |__ _  __| | ___  ___ 
|  __|/ _` | | __/ _` | '__| | | | / _` |/ _` |/ _ \/ __|
| |__| (_| | | || (_| | |    | |/ / (_| | (_| | (_) \__ \
\____/\__,_|_|\__\__,_|_|    |___/ \__,_|\__,_|\___/|___/
"""

def editar_registro(data): # função para editar o registro
    limpar_tela()
    print(titulo_ascii())
    print(Fore.YELLOW + f"\nEdição de Registro do dia {data.strftime('%d/%m/%Y')}\n")

    db = Database()
    registro = db.fetchone("SELECT id, water, energy, organic_waste, recyclable_waste, transport FROM tb_register WHERE user_id = %s AND date = %s", (usuario_logado["id"], data))

    if not registro: # Verifica se o registro existe
        print(Fore.RED + "Registro não encontrado.")
        db.close()
        input("Pressione Enter para voltar...")
        return

    reg_id, water, energy, lixo_org, lixo_rec, transporte = registro # Desempacota os valores do registro

    def novo_valor(label, atual, tipo=float): # Função para editar os valores
        while True:
            val = input(f"{label} atual: {atual} → Novo valor (ou Enter para manter): ").strip()
            if val == "": # Se o usuário pressionar Enter, mantém o valor atual
                return atual
            try:
                return tipo(val)
            except:
                print(Fore.RED + "Valor inválido. Tente novamente.")

    def novo_transporte(atual): # Função para editar o tipo de transporte
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
        escolha = input("Novo tipo (ou Enter para manter): ").strip()
        if escolha == "1": return "sustentável" #se o usuário escolher opção 1, retorna sustentável
        elif escolha == "2": return "misto" # se o usuário escolher opção 2, retorna misto
        elif escolha == "3": return "poluente" # se o usuário escolher opção 3, retorna poluente
        else: return atual # se o usuário pressionar Enter, mantém o valor atual

    # novos valores
    water = novo_valor("→ Água (L)", water)
    energy = novo_valor("→ Energia (kWh)", energy)
    lixo_org = novo_valor("→ Lixo Orgânico (kg)", lixo_org)
    lixo_rec = novo_valor("→ Lixo Reciclável (kg)", lixo_rec)
    transporte = novo_transporte(transporte)

    # Atualiza o registro no banco de dados
    db.execute("""
        UPDATE tb_register
        SET water = %s, energy = %s, organic_waste = %s, recyclable_waste = %s, transport = %s
        WHERE id = %s
    """, (water, energy, lixo_org, lixo_rec, transporte, reg_id))
    db.close()

    print(Fore.GREEN + "\n✅ Registro atualizado com sucesso!")
    input("Pressione Enter para voltar...")

def excluir_registro(data): # função para excluir um registro
    limpar_tela()
    print(titulo_ascii())
    print(Fore.YELLOW + f"\nExclusão de Registro do dia {data.strftime('%d/%m/%Y')}\n")

    db = Database() # Conecta ao banco de dados
    # Verifica se o registro existe
    registro = db.fetchone("SELECT id FROM tb_register WHERE user_id = %s AND date = %s", (usuario_logado["id"], data))

    if not registro: # Se não encontrar o registro, exibe mensagem de erro
        print(Fore.RED + "Registro não encontrado.")
        db.close()
        input("Pressione Enter para voltar...")
        return

    # Confirmação de exclusão
    reg_id = registro[0]
    confirm = input(Fore.RED + "Tem certeza que deseja excluir este registro? (s/n): ").strip().lower()
    if confirm == "s":
        db.execute("DELETE FROM tb_register WHERE id = %s", (reg_id,)) # Exclui o registro
        print(Fore.GREEN + "\n✅ Registro excluído com sucesso!")
    else:
        print(Fore.YELLOW + "\nOperação cancelada.")
    db.close()
    input("Pressione Enter para voltar...")

def editar_ou_excluir(): # Função para editar ou excluir um registro
    limpar_tela()
    print(titulo_ascii())
    print(Fore.YELLOW + "\nEscolha a data do registro que deseja alterar ou excluir:\n")

    # solicita a data ao usuário
    while True:
        data_str = input("Digite a data (dd/mm/aaaa) ou [0] para voltar: ").strip()
        if data_str == "0":
            return
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print(Fore.RED + "❌ Data inválida. Tente novamente.")

    # pergunta ao usuário o que deseja fazer
    print(Fore.YELLOW + "\nO que deseja fazer com esse registro?\n")
    print(Fore.YELLOW + "[1] Editar")
    print(Fore.YELLOW + "[2] Excluir")
    print(Fore.YELLOW + "[0] Cancelar")
    opcao = input("→ Escolha: ").strip()

    # verifica a opção escolhida
    if opcao == "1":
        editar_registro(data)
    elif opcao == "2":
        excluir_registro(data)
    elif opcao == "0":
        return
    else:
        print(Fore.RED + "Opção inválida.")
        input("Pressione Enter para continuar...")
