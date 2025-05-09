import os # Importando a biblioteca os para interações com o sistema operacional
import calendar  # Importando a biblioteca calendar para manipulação de datas
from datetime import datetime # Importando a classe datetime para manipulação de datas e horas
from colorama import Fore, Style, init # Importando a biblioteca colorama para formatação de texto
from banco import Database # Importando a classe Database para interagir com o banco de dados
from sessao import usuario_logado # Importando o dicionário que armazena os dados do usuário logado


init(autoreset=True) # Iniciar colorama


# Definindo a função que limpa a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para exibir o calendário de um mês específico
def exibir_calendario(ano, mes):
    titulo_ascii = Fore.GREEN + Style.BRIGHT + r"""
 _   _ _     _             _           
| | | (_)   | |           (_)          
| |_| |_ ___| |_ ___  _ __ _  ___ ___  
|  _  | / __| __/ _ \| '__| |/ __/ _ \ 
| | | | \__ \ || (_) | |  | | (_| (_) |
\_| |_/_|___/\__\___/|_|  |_|\___\___/ 
"""
    limpar_tela()
    print(Fore.GREEN + Style.BRIGHT + titulo_ascii + "\n")

    # Gerar calendário padrão
    cal = calendar.TextCalendar()
    calendario_original = cal.formatmonth(ano, mes)

    # Obter os dias com registro no banco
    db = Database()
    result = db.fetchall("SELECT date FROM tb_register WHERE user_id = %s", (usuario_logado["id"],))
    db.close()
    dias_registrados = {d[0].day for d in result if d[0].month == mes and d[0].year == ano}

    # Realçar os dias registrados
    linhas = calendario_original.split("\n")
    calendario_colorido = []

    for linha in linhas:
        nova_linha = ""
        for parte in linha.split(" "):
            if parte.strip().isdigit():
                dia = int(parte.strip())
                if dia in dias_registrados:
                    parte = Fore.GREEN + Style.BRIGHT + f"{dia:2}" + Style.RESET_ALL
                else:
                    parte = f"{dia:2}"
            nova_linha += parte + " "
        calendario_colorido.append(nova_linha.rstrip())

    print("\n".join(calendario_colorido)) # Exibe o calendário colorido

# Função para exibir o histórico de registros
def ver_historico():
    ano = datetime.now().year
    mes = datetime.now().month

    while True: 
        exibir_calendario(ano, mes)

        # Exibir opções de navegação
        print(Fore.YELLOW + """
┌──────────────────────────────┐
│ [1] Mês Anterior             │ 
│ [2] Próximo Mês              │
│ [3] Selecionar Dia           │
│ [0] Voltar ao Menu           │
└──────────────────────────────┘
""")
        opcao = input(Fore.WHITE + Style.BRIGHT + "→ Escolha uma opção: ") 

        if opcao == "1": # Se o usuário escolher "1", volta para o mês anterior
            mes -= 1
            if mes < 1:
                mes = 12
                ano -= 1
        elif opcao == "2": # Se o usuário escolher "2", avança para o próximo mês
            mes += 1
            if mes > 12:
                mes = 1
                ano += 1
        elif opcao == "3": # Se o usuário escolher "3", solicita um dia específico
            dia = input(Fore.CYAN + "\nDigite o dia (1-31): ")
            if dia.isdigit() and 1 <= int(dia) <= 31:
                #from relatorio import exibir_relatorio_por_data
                #exibir_relatorio_por_data(dia=int(dia), mes=mes, ano=ano)
                input(Fore.CYAN + "\nPressione Enter para voltar ao histórico...")
            else:
                print(Fore.RED + "❌ Dia inválido.")
                input("Pressione Enter para continuar...")
        elif opcao == "0": # Se o usuário escolher "0", volta para o menu principal
            break
        else: # Se o usuário escolher uma opção inválida, exibe mensagem de erro
            print(Fore.RED + "\n❌ Opção inválida.")
            input("Pressione Enter para continuar...")
