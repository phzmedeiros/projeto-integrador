from colorama import Fore, Style, init
import os
from banco import Database

init(autoreset=True)  # Iniciar colorama

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def registro(dia, mes, ano):
    limpar_tela()
    print(f'Registro de {dia}/{mes}/{ano}')
    check_register(dia, mes, ano)

def check_register(dia, mes, ano):
    db = Database()
    data = f"{ano}-{mes:02d}-{dia:02d}"
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
                from menu import menu_inicial  # Importação local
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


