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

# Função que classifica a pontuação média do dia em três categorias.
# Parâmetro: pontuacao (int) - valor da pontuação média.
# Retorna uma tupla com a classificação textual e a cor correspondente.
def classificar(pontuacao):
    if pontuacao >= 80:
        return "Excelente 🌱", Fore.GREEN
    elif pontuacao >= 50:
        return "Moderado 🌿", Fore.YELLOW
    else:
        return "Ruim 🔥", Fore.RED

# Função que gera uma barra de progresso em ASCII para representar a pontuação.
# Parâmetro: valor (int) - pontuação de 0 a 100.
def gerar_barra(valor):
    blocos = int((valor / 100) * 50)  # Calcula quantos blocos preencher (máximo 50).
    return '▇' * blocos + f" {valor}"

# Função principal que exibe o relatório do dia selecionado pelo usuário.
def relatorio_do_dia():
    limpar_tela()  # Limpa a tela antes de exibir o relatório.

    # Título em ASCII estilizado, exibido em verde e negrito.
    titulo_ascii = Fore.GREEN + Style.BRIGHT + r"""
______     _       _             _           
| ___ \   | |     | |           (_)          
| |_/ /___| | __ _| |_ ___  _ __ _  ___  ___ 
|    // _ \ |/ _` | __/ _ \| '__| |/ _ \/ __|
| |\ \  __/ | (_| | || (_) | |  | | (_) \__ \
\_| \_\___|_|\__,_|\__\___/|_|  |_|\___/|___/
"""
    print(titulo_ascii)

    # Exibe opções para o usuário escolher a data do relatório.
    print(Fore.YELLOW + Style.BRIGHT + "Deseja ver o relatório de qual dia?\n")
    print(Fore.CYAN + """
┌─────────────────────────────┐
│ [1] Relatório de hoje       │
│ [2] Relatório de outro dia  │
│ [0] Voltar                  │
└─────────────────────────────┘
""")
    opcao = input(Fore.CYAN + "→ Escolha: ").strip()

    # Bloco de controle de fluxo para determinar a data do relatório.
    if opcao == "1":
        data = datetime.now().date()  # Usa a data de hoje.
    elif opcao == "2":
        while True:
            data_str = input("Digite a data (dd/mm/aaaa): ").strip()
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y").date()
                break
            except ValueError:
                print(Fore.RED + "Data inválida. Tente novamente.")
    else:
        print(Fore.RED + "Opção inválida.")
        return

    # Verifica se o usuário tem registro para a data escolhida.
    db = Database()
    resultado = db.fetchone(
        "SELECT water, energy, organic_waste, recyclable_waste, transport FROM tb_register WHERE user_id = %s AND date = %s",
        (usuario_logado["id"], data)
    )
    db.close()

    # Se não houver registro, informa o usuário e retorna.
    if not resultado:
        print(Fore.RED + "\nNenhum registro encontrado para essa data.")
        input("Pressione Enter para continuar...")
        return

    # Desempacota os valores do registro retornado do banco.
    water, energy, lixo_org, lixo_rec, transporte = resultado

    # Calcula a pontuação de cada categoria usando as funções de pontuação.
    p1 = pontuar_agua(water)
    p2 = pontuar_energia(energy)
    p3 = pontuar_lixo(lixo_org, lixo_rec)
    p4 = pontuar_transporte(transporte)
    # Calcula a média das pontuações.
    media = int((p1 + p2 + p3 + p4) / 4)

    limpar_tela()  # Limpa a tela antes de exibir o relatório detalhado.
    print(Fore.YELLOW + Style.BRIGHT + f"\nPontuação do dia {data.strftime('%d/%m/%Y')}:")
    
    # Exibe os dados do registro do dia.
    print(Fore.MAGENTA + f"\nResumo do dia:")
    print(Fore.WHITE + f"- Água: {water:.1f} L")
    print(f"- Energia: {energy:.1f} kWh")
    print(f"- Lixo orgânico: {lixo_org:.1f} kg")
    print(f"- Lixo reciclável: {lixo_rec:.1f} kg")
    print(f"- Transporte: {transporte.title()}\n")

    # Exibe barras de pontuação para cada categoria.
    print(Fore.BLUE +   f"Água       | {gerar_barra(p1)}")
    print(Fore.YELLOW + f"Energia    | {gerar_barra(p2)}")
    print(Fore.GREEN +  f"Reciclagem | {gerar_barra(p3)}")
    print(Fore.MAGENTA +f"Transporte | {gerar_barra(p4)}")
    print(Fore.CYAN +   f"Geral      | {gerar_barra(media)}")

    # Classifica a pontuação geral e define a cor da mensagem.
    classificacao, cor = classificar(media)
    print(cor + Style.BRIGHT + f"\nPontuação geral: {media}/100")
    print(cor + Style.BRIGHT + f"Classificação: {classificacao}\n")

    # Mensagem motivacional do urso polar, personalizada conforme a média do dia.
    if media >= 80:
        mensagem = "Parabéns! Seu dia foi incrível para o planeta! Continue assim! 🌎"
    elif media >= 50:
        mensagem = "Bom trabalho! Mas ainda há espaço para melhorar. Pequenas atitudes fazem diferença!"
    else:
        mensagem = "Hoje não foi um bom dia para o meio ambiente... Que tal compensar amanhã?"

    # Arte ASCII de um urso polar, acompanhada da mensagem motivacional.
    urso_polar_ascii = Fore.WHITE + Style.BRIGHT + rf"""
      .--.              .--.
     : (\\ '. _...._ .' //) : 
      '.    '          '  .'
       /'   _        _   '\
      /     ^        ^     \
     |       /      \       |  --<{mensagem}>
     |     /'        '\     |
      \   |    .--.    |   /
       '._\ '  \__/  ' /_.'
       /  ``...-''-...``  \
"""

    print(Fore.CYAN + Style.BRIGHT + "\nMensagem do Urso Polar 🐻‍❄️:")
    print(urso_polar_ascii)

    # Aguarda o usuário pressionar Enter antes de retornar ao menu.
    input("\nPressione Enter para voltar ao menu...")