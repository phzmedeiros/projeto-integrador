# Importa a biblioteca 'os', que permite executar comandos do sistema operacional, como limpar a tela do terminal.
import os

# Importa o módulo 'calendar', utilizado para gerar e manipular calendários.
import calendar

# Importa a classe 'datetime' do módulo 'datetime', usada para manipulação de datas e horas.
from datetime import datetime

# Importa funções e constantes da biblioteca 'colorama' para colorir textos no terminal.
from colorama import Fore, Style, init

# Importa a classe 'Database' do módulo 'banco', responsável pela conexão e operações com o banco de dados.
from banco import Database

# Importa o dicionário 'usuario_logado' do módulo 'sessao', que armazena informações do usuário atualmente autenticado.
from sessao import usuario_logado

# Inicializa o colorama para que as cores sejam resetadas automaticamente após cada print.
init(autoreset=True)

# Função para limpar a tela do terminal, tornando a interface mais amigável.
def limpar_tela():
    # Se o sistema operacional for Windows, executa 'cls', senão executa 'clear' (Linux/Mac).
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que retorna um texto ASCII estilizado para ser usado como título na tela de histórico.
def titulo_ascii():
    # Retorna uma string com arte ASCII, usando cor verde e estilo negrito.
    return Fore.GREEN + Style.BRIGHT + r"""
 _   _ _     _             _           
| | | (_)   | |           (_)          
| |_| |_ ___| |_ ___  _ __ _  ___ ___  
|  _  | / __| __/ _ \| '__| |/ __/ _ \ 
| | | | \__ \ || (_) | |  | | (_| (_) |
\_| |_/_|___/\__\___/|_|  |_|\___\___/ 
"""

# Função responsável por exibir o calendário do mês, destacando os dias com registros.
# Parâmetros:
#   ano: ano a ser exibido no calendário.
#   mes: mês a ser exibido.
#   dias_registrados: conjunto com os dias do mês que possuem registros no banco.
def exibir_calendario(ano, mes, dias_registrados):
    cal = calendar.TextCalendar()  # Cria um objeto de calendário textual.
    calendario_original = cal.formatmonth(ano, mes)  # Gera o calendário do mês como string.
    linhas = calendario_original.split("\n")  # Divide o calendário em linhas.
    calendario_colorido = []  # Lista para armazenar as linhas coloridas.

    # Percorre cada linha do calendário.
    for linha in linhas:
        nova_linha = ""  # Inicializa a nova linha colorida.
        # Divide a linha em partes (dias e espaços).
        for parte in linha.split(" "):
            # Verifica se a parte é um número (dia do mês).
            if parte.strip().isdigit():
                dia = int(parte.strip())
                # Se o dia está em dias_registrados, colore de verde e negrito.
                if dia in dias_registrados:
                    parte = Fore.GREEN + Style.BRIGHT + f"{dia:2}" + Style.RESET_ALL
                else:
                    parte = f"{dia:2}"  # Mantém o dia sem cor.
            nova_linha += parte + " "  # Adiciona a parte à nova linha.
        calendario_colorido.append(nova_linha.rstrip())  # Adiciona a linha à lista.
    return "\n".join(calendario_colorido)  # Retorna o calendário colorido como string.

# Função principal para visualizar o histórico de registros do usuário.
def ver_historico():
    # Define o ano e mês atuais como padrão para exibição inicial.
    ano = datetime.now().year
    mes = datetime.now().month

    # Loop principal para navegação no histórico.
    while True:
        limpar_tela()  # Limpa a tela para melhor visualização.
        print(titulo_ascii())  # Exibe o título estilizado.

        db = Database()  # Cria uma instância do banco de dados.
        # Busca todas as datas de registros do usuário logado.
        result = db.fetchall("SELECT date FROM tb_register WHERE user_id = %s", (usuario_logado["id"],))
        if result:
            dias_registrados = {d[0].day for d in result if d[0] and d[0].month == mes and d[0].year == ano}
        else:
            dias_registrados = set()
        # Exibe o calendário do mês, destacando os dias com registros.
        print(exibir_calendario(ano, mes, dias_registrados))
        # Exibe o menu de navegação do histórico.
        print(Fore.CYAN + """
┌───────────────────────────────────────────────┐
│ [1] Mês Anterior                              │ 
│ [2] Próximo Mês                               │
│ [3] Selecionar Dia com Registro               │
│ [0] Voltar ao Menu                            │
└───────────────────────────────────────────────┘
""")

        # Solicita ao usuário a escolha de uma opção do menu.
        opcao = input(Fore.CYAN + "→ Escolha uma opção: ").strip()

        # Se o usuário escolher "1", vai para o mês anterior.
        if opcao == "1":
            mes -= 1
            if mes < 1:
                mes = 12
                ano -= 1
        # Se escolher "2", vai para o próximo mês.
        elif opcao == "2":
            mes += 1
            if mes > 12:
                mes = 1
                ano += 1
        # Se escolher "3", permite selecionar um dia específico com registro.
        elif opcao == "3":
            dia = input("Digite o dia (1-31): ").strip()
            # Valida se o dia informado é um número entre 1 e 31.
            if not dia.isdigit() or not (1 <= int(dia) <= 31):
                print(Fore.RED + "❌ Dia inválido.")
                input("Pressione Enter para continuar...")
                continue
            
            # Cria um objeto data com o ano, mês e dia informados.
            data = datetime(ano, mes, int(dia)).date()
            db = Database()  # Nova conexão com o banco.
            # Busca o registro do usuário para a data selecionada.
            registro = db.fetchone("SELECT water, energy, organic_waste, recyclable_waste, transport FROM tb_register WHERE user_id = %s AND date = %s", (usuario_logado["id"], data))
            db.close()

            # Se não houver registro para o dia, informa o usuário.
            if not registro:
                print(Fore.RED + "\n❌ Nenhum registro encontrado neste dia.")
                input("Pressione Enter para continuar...")
                continue

            # Desempacota os valores do registro retornado do banco.
            agua, energia, lixo_org, lixo_rec, transporte = registro
            # Calcula a pontuação média do dia usando as funções de pontuação.
            media = int((pontuar_agua(agua) + pontuar_energia(energia) + pontuar_lixo(lixo_org, lixo_rec) + pontuar_transporte(transporte)) / 4)

            # Limpa a tela e exibe os dados detalhados do registro selecionado.
            limpar_tela()
            print(Fore.CYAN + Style.BRIGHT + f"\nRegistro do dia {data.strftime('%d/%m/%Y')}")
            print(Fore.WHITE + f"- Água: {agua:.1f} L")
            print(f"- Energia: {energia:.1f} kWh")
            print(f"- Lixo orgânico: {lixo_org:.1f} kg")
            print(f"- Lixo reciclável: {lixo_rec:.1f} kg")
            print(f"- Transporte: {transporte.title()}")
            print(Fore.GREEN + Style.BRIGHT + f"\nPontuação média: {media}/100\n")

            # Exibe opções para editar ou excluir o registro, ou voltar.
            print(Fore.YELLOW + """
[1] Editar Registro
[2] Excluir Registro
[0] Voltar
""")
            acao = input("→ Escolha uma ação: ").strip()

            # Se o usuário escolher "1", importa e chama a função para editar o registro.
            if acao == "1":
                from editar_excluir import editar_registro
                editar_registro(data)
            # Se escolher "2", importa e chama a função para excluir o registro.
            elif acao == "2":
                from editar_excluir import excluir_registro
                excluir_registro(data)
            else:
                continue  # Qualquer outra opção volta para o início do loop.

        # Se escolher "0", sai do loop e retorna ao menu anterior.
        elif opcao == "0":
            break
        else:
            # Se a opção for inválida, informa o erro e solicita nova entrada.
            print(Fore.RED + "❌ Opção inválida.")
            input("Pressione Enter para continuar...")

# Função que calcula a pontuação do consumo de água.
# Parâmetro: valor (float) - quantidade de água consumida em litros.
def pontuar_agua(valor):
    if valor <= 100: return 100  # Consumo excelente.
    if valor <= 150: return 80   # Consumo bom.
    if valor <= 200: return 60   # Consumo razoável.
    if valor <= 250: return 40   # Consumo alto.
    if valor <= 300: return 20   # Consumo muito alto.
    if valor > 300: return 0     # Consumo excessivo.

# Função que calcula a pontuação do consumo de energia elétrica.
# Parâmetro: valor (float) - quantidade de energia consumida em kWh.
def pontuar_energia(valor):
    if valor <= 4: return 100    # Consumo excelente.
    if valor <= 6: return 80     # Consumo bom.
    if valor <= 9: return 60     # Consumo razoável.
    if valor <= 12: return 40    # Consumo alto.
    if valor <= 15: return 20    # Consumo muito alto.
    if valor > 15: return 0      # Consumo excessivo.

# Função que calcula a pontuação do descarte de lixo.
# Parâmetros:
#   org (float): quantidade de lixo orgânico.
#   rec (float): quantidade de lixo reciclável.
def pontuar_lixo(org, rec):
    total = org + rec  # Soma o total de lixo produzido.
    if total == 0: return 100  # Se não produziu lixo, pontuação máxima.
    proporcao = rec / total  # Calcula a proporção de lixo reciclável.
    if proporcao >= 0.8: return 100  # Excelente reciclagem.
    if proporcao >= 0.5: return 80   # Boa reciclagem.
    if proporcao >= 0.3: return 50   # Reciclagem razoável.
    return 20                        # Reciclagem baixa.

# Função que calcula a pontuação do tipo de transporte utilizado.
# Parâmetro: tipo (str) - tipo de transporte (sustentável, misto ou poluente).
def pontuar_transporte(tipo):
    if tipo == "sustentável": return 100  # Transporte sustentável.
    if tipo == "misto": return 60         # Transporte misto.
    return 20                             # Transporte poluente ou outro.