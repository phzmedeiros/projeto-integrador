<<<<<<< HEAD
from colorama import Fore, Style, init
import os
from tela_boas_vindas import tela_boas_vindas
#biblioteca para trabalhar com o calendario
import calendar
#biblioteca para pegar a data atual
import datetime
from datetime import datetime
from banco import Database


init(autoreset=True)  # Iniciar colorama
=======
import os
from datetime import datetime
from colorama import Fore, Style, init
from banco import Database
from sessao import usuario_logado

init(autoreset=True)
>>>>>>> feature/pedro

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

<<<<<<< HEAD

def registro(dia,mes,ano):
    limpar_tela()
    print(f'Registro de {dia}/{mes}/{ano}')
    check_register(dia, mes, ano)



def check_register(dia, mes, ano):
    # abrir o banco de dados
    db = Database()

    # formatar a data no formato esperado pelo banco de dados (YYYY-MM-DD)
    data = f"{ano}-{mes:02d}-{dia:02d}"

    # query
    registro = db.fetchone("SELECT * FROM tb_register WHERE date = %s", (data,))
    db.close()

    if registro:
        print(Fore.GREEN + f"\n✅ Registro encontrado nesta data.\n")
    else:
        print(Fore.RED + f"\n❌ Nenhum registro encontrado nesta data. Gostaria de cadastrar?\n")
        print(Fore.YELLOW + """
┌──────────────────────────────┐
│ [1] Sim                      │ 
│ [2] Não, voltar para o menu  │
└──────────────────────────────┘
""")
        while True:
            opcao = input(Fore.WHITE + Style.BRIGHT + "Escolha uma opção: ")
            if opcao == "1":
                cadastrar_registro(dia, mes, ano)
                break
            elif opcao == "2":
                from menu import menu_inicial
                menu_inicial()
                break
            else:
                print(Fore.RED + "\nOpção inválida. Tente novamente.\n")
                

def cadastrar_registro(dia, mes, ano):
    limpar_tela()
    print(f"Cadastro para a data {dia}/{mes}/{ano}\n")
    menu_lateral = Fore.YELLOW + """
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Digite [0] para voltar ao menu                                         │
 └────────────────────────────────────────────────────────────────────────┘
"""
    print(menu_lateral)
    #agua consumida
    while True:
        try:
            water = input(Fore.BLUE +"\n💧 Agua consumida (em litros): ") 
            if water == "0":
                from menu import menu_inicial
                menu_inicial()
                break
            break
        except ValueError:
            print(Fore.RED + "\n❌ Valor inválido. Tente novamente.\n")
            continue

    #energia consumida
    while True:
        try:
            energy = input(Fore.YELLOW +"\n⚡ Energia consumida (em kWh): ") 
            if energy == "0":
                from menu import menu_inicial
                menu_inicial()
                break
            break
        except ValueError:
            print(Fore.RED + "\n❌ Valor inválido. Tente novamente.\n")
            continue

    #reciduos não reciclaveis
    while True:
        try:
            waste = input(Fore.WHITE +"\n🗑️  Resíduos não recicláveis (em kg): ") 
            if waste == "0":
                from menu import menu_inicial
                menu_inicial()
                break
            break
        except ValueError:
            print(Fore.RED + "\n❌ Valor inválido. Tente novamente.\n")
            continue

    #resciduos reciclaveis
    while True:
        try:
            rwaste = input(Fore.GREEN +"\n♻️  Resíduos recicláveis (em kg): ") 
            if rwaste == "0":
                from menu import menu_inicial
                menu_inicial()
                break
            break
        except ValueError:
            print(Fore.RED + "\n❌ Valor inválido. Tente novamente.\n")
            continue
    
    #transporte
    while True:
        print("\nEscolha sua opção de transporte: \n")
        print(Fore.YELLOW + """

 [1] Rransporte publico 🚌 
 [2] Bicicleta 🚲          
 [3] Caminhada 🚶‍♂️           
 [4] Carro (Fóssil) 🚗     
 [5] Carro Elétrico 🚗⚡            

""")
        
        opcao_trans = input(Fore.WHITE + Style.BRIGHT + "Escolha uma opção: ")

        if opcao_trans == "1":
            transport = "transporte_publico"
            break
        elif opcao_trans == "2":
            transport = "bicicleta"
            break
        elif opcao_trans == "3":
            transport = "caminhada"
            break
        elif opcao_trans == "4":
            transport = "carro_fossil"
            break
        elif opcao_trans == "5":
            transport = "carro_eletrico"
            break
        elif opcao_trans == "0":
            from menu import menu_inicial
            menu_inicial()
            break
        else:
            print(Fore.RED + "\n❌ Opção inválida. Tente novamente.\n")
            continue
    
    # abrir o banco de dados
    db = Database()

    #formatar a data no formato esperado pelo banco de dados (YYYY-MM-DD)
    data = f"{ano}-{mes:02d}-{dia:02d}"

    # query para inserir o registro
    db.execute("INSERT INTO tb_register (user_id,date,water,energy,organic_waste,recyclable_waste,transport) VALUES (%s)",
               (1,data,float(water),float(energy),float(waste),float(rwaste),transport))

    db.close()

    print(Fore.GREEN + f"\n✅ Registro cadastrado com sucesso na data {data}.\n")
    input(Fore.CYAN + "Pressione [Enter] para continuar...")
    from menu import menu_inicial
    menu_inicial()


=======
def registro(dia=None, mes=None, ano=None):
    limpar_tela()

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

    print(Fore.YELLOW + Style.BRIGHT + "Escolha o tipo de registro:")
    hoje = datetime.now()
    print(Fore.CYAN + f"""
╔═════════════════════════════════════════════════════════════════╗
║                        Tipo de Registro                         ║
╠═════════════════════════════════════════════════════════════════╣
║ [1] Registrar o dia de hoje     ({hoje.strftime('%d/%m/%Y')})                    ║
║ [2] Escolher outro dia                                          ║
║ [0] Voltar ao menu                                              ║
╚═════════════════════════════════════════════════════════════════╝
""")

    while True:
        escolha = input(Fore.WHITE + Style.BRIGHT + "→ Escolha uma opção: ").strip()
        if escolha == "1":
            data_registro = hoje.date()
            break
        elif escolha == "2":
            while True:
                data_str = input("Digite a data (dd/mm/aaaa): ").strip()
                try:
                    data_registro = datetime.strptime(data_str, "%d/%m/%Y").date()
                    break
                except ValueError:
                    print(Fore.RED + "Data inválida. Tente novamente.")
            break
        elif escolha == "0":
            from menu import menu
            menu()
            return
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

    limpar_tela()
    print(Fore.YELLOW + f"\nRegistro do dia {data_registro.strftime('%d/%m/%Y')}\n")

    # Entrada de dados com tratamento individual para melhor didática
    while True:
        try:
            agua = float(input("→ Consumo de água (litros): ").strip())
            if agua < 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número positivo para a água.")

    while True:
        try:
            energia = float(input("→ Consumo de energia elétrica (kWh): ").strip())
            if energia < 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número positivo para a energia.")

    while True:
        try:
            lixo_organico = float(input("→ Quantidade de lixo orgânico (kg): ").strip())
            if lixo_organico < 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número positivo para o lixo orgânico.")

    while True:
        try:
            lixo_reciclavel = float(input("→ Quantidade de lixo reciclável (kg): ").strip())
            if lixo_reciclavel < 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número positivo para o lixo reciclável.")

    print(Fore.YELLOW + """
╔════════════════════════════════════════════════════════════════╗
║          Categoria de Transporte Utilizado no Dia              ║
╠═════════════════╦══════════════════════════════════════════════╣
║ [1] Sustentável ║ A pé, bicicleta, skate, patinete elétrico    ║
║ [2] Misto       ║ Carro elétrico, transporte público, carona   ║
║ [3] Poluente    ║ Moto, carro a combustão, avião               ║
╚═════════════════╩══════════════════════════════════════════════╝
""")

    mapa_categorias = {
        "1": "sustentável",
        "2": "misto",
        "3": "poluente"
    }

    while True:
        tipo_transporte = input("→ Escolha a categoria (1/2/3): ").strip()
        if tipo_transporte in mapa_categorias:
            transporte = mapa_categorias[tipo_transporte]
            break
        else:
            print(Fore.RED + "Opção inválida. Digite 1, 2 ou 3.")

    db = Database()
    db.execute("""
        INSERT INTO tb_register (user_id, date, water, energy, organic_waste, recyclable_waste, transport)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (usuario_logado["id"], data_registro, agua, energia, lixo_organico, lixo_reciclavel, transporte))
    db.close()

    print(Fore.GREEN + f"\nRegistro do dia {data_registro.strftime('%d/%m/%Y')} salvo com sucesso!")
    input(Fore.YELLOW + "Pressione Enter para continuar...")
>>>>>>> feature/pedro
