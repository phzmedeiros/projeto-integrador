import os
from datetime import datetime
from colorama import Fore, Style, init
from banco import Database
from sessao import usuario_logado

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pontuar_agua(valor):
    if valor <= 100: return 100
    if valor <= 150: return 70
    if valor <= 200: return 50
    return 20

def pontuar_energia(valor):
    if valor <= 10: return 100
    if valor <= 20: return 70
    if valor <= 30: return 50
    return 20

def pontuar_lixo(org, rec):
    total = org + rec
    if total == 0: return 100
    proporcao = rec / total
    if proporcao >= 0.8: return 100
    if proporcao >= 0.5: return 70
    if proporcao >= 0.3: return 50
    return 20

def pontuar_transporte(tipo):
    if tipo == "sustentável": return 100
    if tipo == "misto": return 60
    return 20

def classificar(pontuacao):
    if pontuacao >= 80:
        return "Excelente 🌱", Fore.GREEN
    elif pontuacao >= 50:
        return "Moderado 🌿", Fore.YELLOW
    else:
        return "Ruim 🔥", Fore.RED

def gerar_barra(valor):
    blocos = int((valor / 100) * 50)
    return '▇' * blocos + f" {valor}"

def relatorio_do_dia():
    limpar_tela()
    titulo_ascii = Fore.GREEN + Style.BRIGHT + r"""
______     _       _             _           
| ___ \   | |     | |           (_)          
| |_/ /___| | __ _| |_ ___  _ __ _  ___  ___ 
|    // _ \ |/ _` | __/ _ \| '__| |/ _ \/ __|
| |\ \  __/ | (_| | || (_) | |  | | (_) \__ \
\_| \_\___|_|\__,_|\__\___/|_|  |_|\___/|___/
"""
    print(titulo_ascii)

    print(Fore.YELLOW + Style.BRIGHT + "Deseja ver o relatório de qual dia?\n")
    print(Fore.CYAN + """
┌─────────────────────────────┐
│ [1] Relatório de hoje       │
│ [2] Relatório de outro dia  │
│ [0] Voltar para o menu      │
└─────────────────────────────┘
""")
    opcao = input(Fore.CYAN + "→ Escolha: ").strip()

    if opcao == "1":
        data = datetime.now().date()
    elif opcao == "2":
        while True:
            data_str = input("Digite a data (dd/mm/aaaa): ").strip()
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y").date()
                break
            except ValueError:
                print(Fore.RED + "Data inválida. Tente novamente.")
    elif opcao == "0":
        from menu import menu
        menu()
        return
    else:
        print(Fore.RED + "Opção inválida.")
        return

    db = Database()
    resultado = db.fetchone("SELECT water, energy, organic_waste, recyclable_waste, transport FROM tb_register WHERE user_id = %s AND date = %s", (usuario_logado["id"], data))
    db.close()

    if not resultado:
        print(Fore.RED + "\nNenhum registro encontrado para essa data.")
        input("Pressione Enter para continuar...")
        return

    water, energy, lixo_org, lixo_rec, transporte = resultado
    p1 = pontuar_agua(water)
    p2 = pontuar_energia(energy)
    p3 = pontuar_lixo(lixo_org, lixo_rec)
    p4 = pontuar_transporte(transporte)
    media = int((p1 + p2 + p3 + p4) / 4)

    limpar_tela()
    print(Fore.YELLOW + Style.BRIGHT + f"\nPontuação do dia {data.strftime('%d/%m/%Y')}:")

    print(Fore.MAGENTA + f"\nResumo do dia:")
    print(Fore.WHITE + f"- Água: {water:.1f} L")
    print(f"- Energia: {energy:.1f} kWh")
    print(f"- Lixo orgânico: {lixo_org:.1f} kg")
    print(f"- Lixo reciclável: {lixo_rec:.1f} kg")
    print(f"- Transporte: {transporte.title()}\n")

    print(Fore.BLUE +   f"Água       | {gerar_barra(p1)}")
    print(Fore.YELLOW + f"Energia    | {gerar_barra(p2)}")
    print(Fore.GREEN +  f"Reciclagem | {gerar_barra(p3)}")
    print(Fore.MAGENTA +f"Transporte | {gerar_barra(p4)}")
    print(Fore.CYAN +   f"Geral      | {gerar_barra(media)}")

    classificacao, cor = classificar(media)
    print(cor + Style.BRIGHT + f"\nPontuação geral: {media}/100")
    print(cor + Style.BRIGHT + f"Classificação: {classificacao}\n")

    if media >= 80:
        mensagem = "Parabéns! Seu dia foi incrível para o planeta! Continue assim! 🌎"
    elif media >= 50:
        mensagem = "Bom trabalho! Mas ainda há espaço para melhorar. Pequenas atitudes fazem diferença!"
    else:
        mensagem = "Hoje não foi um bom dia para o meio ambiente... Que tal compensar amanhã?"

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

    input("\nPressione Enter para voltar ao menu...")