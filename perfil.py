import os
from colorama import Fore, Style, init
from banco import Database
from sessao import usuario_logado

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo_ascii():
    return Fore.GREEN + Style.BRIGHT + r"""
 _   _       _     _ _   _____                       │  ______          __ _ _ 
| | | |     | |   (_) | |  __ \                      │  | ___ \        / _(_) |
| |_| | __ _| |__  _| |_| |  \/_ __ ___  ___ _ __    │  | |_/ /__ _ __| |_ _| |
|  _  |/ _` | '_ \| | __| | __| '__/ _ \/ _ \ '_ \   │  |  __/ _ \ '__|  _| | |
| | | | (_| | |_) | | |_| |_\ \ | |  __/  __/ | | |  │  | | |  __/ |  | | | | |
\_| |_/\__,_|_.__/|_|\__|\____/_|  \___|\___|_| |_|  │  \_|  \___|_|  |_| |_|_|
"""

def calcular_media_geral(registros):
    if not registros:
        return 0
    total = 0
    for r in registros:
        total += (pontuar_agua(r[0]) + pontuar_energia(r[1]) + pontuar_lixo(r[2], r[3]) + pontuar_transporte(r[4])) / 4
    return int(total / len(registros))

def media_individual(registros, index):
    if not registros:
        return 0.0
    return round(sum(r[index] for r in registros) / len(registros), 1)

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

def barra_ascii(valor):
    blocos = int((valor / 100) * 40)
    return "▇" * blocos + f" {valor}/100"

def perfil_usuario(user_id):
    while True:
        limpar_tela()
        print(titulo_ascii())

        db = Database()
        user = db.fetchone("SELECT cli_name, cli_email, cli_cpf FROM tb_client WHERE cli_id = %s", (user_id,))
        registros = db.fetchall("SELECT water, energy, organic_waste, recyclable_waste, transport FROM tb_register WHERE user_id = %s", (user_id,))

        nome, email, cpf = user
        media_geral = calcular_media_geral(registros)
        media_agua = media_individual(registros, 0)
        media_energia = media_individual(registros, 1)
        media_lixo_org = media_individual(registros, 2)
        media_lixo_rec = media_individual(registros, 3)

        print(Fore.GREEN + Style.BRIGHT + f"\nOlá, {nome}! Bem-vindo(a) ao seu perfil no HabitGreen!\n")
        print(Fore.WHITE + Style.BRIGHT + f"E-mail: {email}")
        print(Fore.WHITE + Style.BRIGHT + f"CPF: {cpf}")
        print(Fore.GREEN + "\nSustentabilidade Geral:")
        print(Fore.GREEN + barra_ascii(media_geral))

        print(Fore.GREEN + "\nMédias gerais dos seus registros:")
        print(Fore.WHITE + f"- Água: {media_agua} L")
        print(f"- Energia: {media_energia} kWh")
        print(f"- Lixo Orgânico: {media_lixo_org} kg")
        print(f"- Lixo Reciclável: {media_lixo_rec} kg")

        if media_geral >= 80:
            mensagem = "Incrível! Você está contribuindo muito com o planeta! 🌎"
        elif media_geral >= 50:
            mensagem = "Você está indo bem, continue melhorando suas práticas diárias! 🌿"
        else:
            mensagem = "Atenção! Pequenas mudanças podem gerar um grande impacto! 🍃"

        urso_ascii = Fore.WHITE + Style.BRIGHT + rf'''
      .--.              .--.
     : (\\ '. _...._ .' //) : 
      '.    '          '  .'
       /'   _        _   '\
      /     ^        ^     \
     |       /      \       | --< {mensagem} >
     |     /'        '\     |
      \   |    .--.    |   /
       '._\ '  \__/  ' /_.'
       /  ``...-''-...``  \
'''
        print(Fore.GREEN + "\nMensagem do Urso Polar:")
        print(urso_ascii)

        print(Fore.YELLOW + """
┌─────────────────────────────┐
│ [1] Alterar dados do perfil │
│ [0] Voltar ao menu          │
└─────────────────────────────┘
""")
        opcao = input(Fore.GREEN + "→ Escolha uma opção: ").strip()

        if opcao == "1":
            nome_novo = input("Novo nome (ou Enter para manter): ").strip()
            email_novo = input("Novo e-mail (ou Enter para manter): ").strip()
            cpf_novo = input("Novo CPF (ou Enter para manter): ").strip()
            senha_nova = input("Nova senha (ou Enter para manter): ").strip()

            if nome_novo == "": nome_novo = nome
            if email_novo == "": email_novo = email
            if cpf_novo == "": cpf_novo = cpf

            if senha_nova != "":
                db.execute("UPDATE tb_client SET cli_name=%s, cli_email=%s, cli_cpf=%s, cli_password=%s WHERE cli_id=%s",
                           (nome_novo, email_novo, cpf_novo, senha_nova, user_id))
            else:
                db.execute("UPDATE tb_client SET cli_name=%s, cli_email=%s, cli_cpf=%s WHERE cli_id=%s",
                           (nome_novo, email_novo, cpf_novo, user_id))
            print(Fore.GREEN + "\n✅ Dados atualizados com sucesso!")
            input("Pressione Enter para continuar...")
        elif opcao == "0":
            db.close()
            break
        else:
            print(Fore.RED + "Opção inválida.")
            input("Pressione Enter para continuar...")
