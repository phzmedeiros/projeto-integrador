import os
import calendar
from datetime import datetime
from colorama import Fore, Style, init
from banco import Database
from sessao import usuario_logado

init(autoreset=True) # Iniciar colorama

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo_ascii():
    return Fore.GREEN + Style.BRIGHT + r"""
 _   _ _     _             _           
| | | (_)   | |           (_)          
| |_| |_ ___| |_ ___  _ __ _  ___ ___  
|  _  | / __| __/ _ \| '__| |/ __/ _ \ 
| | | | \__ \ || (_) | |  | | (_| (_) |
\_| |_/_|___/\__\___/|_|  |_|\___\___/ 
"""

def exibir_calendario(ano, mes, dias_registrados): # Função para exibir o calendário
    cal = calendar.TextCalendar() # Cria um calendário
    calendario_original = cal.formatmonth(ano, mes) # Formata o mês 
    linhas = calendario_original.split("\n") # Divide o calendário em linhas
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
    return "\n".join(calendario_colorido)

def ver_historico(): 
    ano = datetime.now().year
    mes = datetime.now().month

    while True:
        limpar_tela()
        print(titulo_ascii())

        db = Database()
        result = db.fetchall("SELECT date FROM tb_register WHERE user_id = %s", (usuario_logado["id"],))
        db.close()
        dias_registrados = {d[0].day for d in result if d[0].month == mes and d[0].year == ano}

        # menu de navegação de histórico por datas 
        print(exibir_calendario(ano, mes, dias_registrados))
        print(Fore.CYAN + """
┌───────────────────────────────────────────────┐
│ [1] Mês Anterior                              │ 
│ [2] Próximo Mês                               │
│ [3] Selecionar Dia com Registro               │
│ [0] Voltar ao Menu                            │
└───────────────────────────────────────────────┘
""")

        opcao = input(Fore.CYAN + "→ Escolha uma opção: ").strip()

        if opcao == "1":
            mes -= 1 
            if mes < 1:
                mes = 12
                ano -= 1
        elif opcao == "2":
            mes += 1 
            if mes > 12:
                mes = 1
                ano += 1
        elif opcao == "3":
            dia = input("Digite o dia (1-31): ").strip()
            if not dia.isdigit() or not (1 <= int(dia) <= 31):
                print(Fore.RED + "❌ Dia inválido.")
                input("Pressione Enter para continuar...")
                continue
            
            #busca o registro no banco de dados
            data = datetime(ano, mes, int(dia)).date()
            db = Database()
            registro = db.fetchone("SELECT water, energy, organic_waste, recyclable_waste, transport FROM tb_register WHERE user_id = %s AND date = %s", (usuario_logado["id"], data))
            db.close()

            if not registro: # Se não houver registro, exibe mensagem de erro
                print(Fore.RED + "\n❌ Nenhum registro encontrado neste dia.")
                input("Pressione Enter para continuar...")
                continue

            #calcula a pontuação média
            agua, energia, lixo_org, lixo_rec, transporte = registro
            media = int((pontuar_agua(agua) + pontuar_energia(energia) + pontuar_lixo(lixo_org, lixo_rec) + pontuar_transporte(transporte)) / 4)

            # Exibe os dados do registro
            limpar_tela()
            print(Fore.CYAN + Style.BRIGHT + f"\nRegistro do dia {data.strftime('%d/%m/%Y')}")
            print(Fore.WHITE + f"- Água: {agua:.1f} L")
            print(f"- Energia: {energia:.1f} kWh")
            print(f"- Lixo orgânico: {lixo_org:.1f} kg")
            print(f"- Lixo reciclável: {lixo_rec:.1f} kg")
            print(f"- Transporte: {transporte.title()}")
            print(Fore.GREEN + Style.BRIGHT + f"\nPontuação média: {media}/100\n")

            # Opções de edição ou exclusão do registro
            print(Fore.YELLOW + """
[1] Editar Registro
[2] Excluir Registro
[0] Voltar
""")
            acao = input("→ Escolha uma ação: ").strip()

            if acao == "1":
                from editar_excluir import editar_registro
                editar_registro(data)
            elif acao == "2":
                from editar_excluir import excluir_registro
                excluir_registro(data)
            else:
                continue

        elif opcao == "0":
            break
        else:
            print(Fore.RED + "❌ Opção inválida.")
            input("Pressione Enter para continuar...")

# Funções de pontuação importadas aqui para manter compatibilidade
def pontuar_agua(valor):
    if valor <= 100: return 100
    if valor <= 150: return 80
    if valor <= 200: return 60
    if valor <= 250: return 40
    if valor <= 300: return 20
    if valor > 300: return 0

def pontuar_energia(valor):
    if valor <= 4: return 100
    if valor <= 6: return 80
    if valor <= 9: return 60
    if valor <= 12: return 40
    if valor <= 15: return 20   
    if valor > 15: return 0

def pontuar_lixo(org, rec):
    total = org + rec
    if total == 0: return 100
    proporcao = rec / total
    if proporcao >= 0.8: return 100
    if proporcao >= 0.5: return 80
    if proporcao >= 0.3: return 50
    return 20

def pontuar_transporte(tipo):
    if tipo == "sustentável": return 100
    if tipo == "misto": return 60
    return 20
