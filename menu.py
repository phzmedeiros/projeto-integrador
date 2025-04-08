from colorama import Fore, Style, init
import os
<<<<<<< HEAD
from tela_boas_vindas import tela_boas_vindas
#biblioteca para trabalhar com o calendario
import calendar
#biblioteca para pegar a data atual
import datetime
from datetime import datetime
from registro import registro


init(autoreset=True)  # Iniciar colorama
=======
from sessao import usuario_logado
init(autoreset=True)
>>>>>>> feature/pedro

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

<<<<<<< HEAD
def menu_inicial():
    limpar_tela()

    titulo_ascii = Fore.GREEN + Style.BRIGHT +"""
 _    _           _       _   _      _____                              
| |  | |         | |     (_) | |    / ____|                             
| |__| |   __ _  | |__    _  | |_  | |  __   _ __    ___    ___   _ __  
|  __  |  / _` | | '_ \  | | | __| | | |_ | | '__|  / _ \  / _ \ | '_ \ 
| |  | | | (_| | | |_) | | | | |_  | |__| | | |    |  __/ |  __/ | | | |
|_|  |_|  \__,_| |_.__/  |_|  \__|  \_____| |_|     \___|  \___| |_| |_|              
"""
    menu_lateral = Fore.YELLOW + """
 ┌─────────────────────────────────────────────────────────────────┐
 │ Selecione quais são os dados sustentaveis que você quer acessar │                            
 └─────────────────────────────────────────────────────────────────┘
"""

    opcoes = Fore.CYAN + Style.BRIGHT + """
┌────────────────┐
│ Opções:        │
│                │
│ [1] Calendario │
│ [2] Histórico  │
│ [3] perfil     │
│ [4] Sair       │
└────────────────┘
"""
    print(f"{titulo_ascii}{menu_lateral}" + opcoes)
    
    while True:
        opcao = input(Fore.WHITE + Style.BRIGHT + "Digite a opção escolhida: ")
        if opcao == "1":
            calendario()
            break
        elif opcao == "2":
            #perfil
            break
        elif opcao == "3":
            #perfil
            break
        elif opcao == "4":
            tela_boas_vindas()
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")



def exibir_calendario(ano, mes):
    titulo_ascii = Fore.GREEN + Style.BRIGHT +"""
   _____           _                      _                  _         
  / ____|         | |                    | |                (_)        
 | |        __ _  | |   ___   _ __     __| |   __ _   _ __   _    ___  
 | |       / _` | | |  / _ \ | '_ \   / _` |  / _` | | '__| | |  / _ \ 
 | |____  | (_| | | | |  __/ | | | | | (_| | | (_| | | |    | | | (_) |
  \_____|  \__,_| |_|  \___| |_| |_|  \__,_|  \__,_| |_|    |_|  \___/ 
                                                                       
                                                                              
"""
    limpar_tela()
    #pagar a função de exibir o calendário da biblioteca 'calendar'
    print(Fore.GREEN + Style.BRIGHT + titulo_ascii,"\n")
    cal = calendar.TextCalendar()
    print(Fore.CYAN + cal.formatmonth(ano, mes))

def calendario():

    ano = int(datetime.now().year)  # Ano atual
    mes = int(datetime.now().month) # Mês atual 
    
 
    while True:
        exibir_calendario(ano, mes)
        
        print(Fore.YELLOW + """
┌──────────────────────────────┐
│ [1] Mês Anterior             │ 
│ [2] Próximo Mês              │
│ [3] Selecionar Dia de Hoje   │
│ [4] Selecionar Outro Dia     │
│ [0] Voltar ao Menu           │
└──────────────────────────────┘
""")
        opcao = input(Fore.WHITE + Style.BRIGHT + "Escolha uma opção: ")
        
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
            dia = int(datetime.now().day)
            mes = int(datetime.now().month)
            ano = int(datetime.now().year)


            registro(dia, mes, ano)
            break

        elif opcao == "4":
            dia = input(Fore.WHITE + "\nDigite o dia (1-31): ")
            if dia.isdigit() and 1 <= int(dia) <= 31:
                
                registro(int(dia), mes, ano)
                break
            else:
                print(Fore.RED + "Dia inválido. Tente novamente.")
        elif opcao == "0":
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

limpar_tela()
menu_inicial()

=======
def menu():
    while True:
        limpar_tela()
        print(Fore.GREEN + Style.BRIGHT + r"""
 _   _       _     _ _   _____                     
| | | |     | |   (_) | |  __ \                    
| |_| | __ _| |__  _| |_| |  \/_ __ ___  ___ _ __  
|  _  |/ _` | '_ \| | __| | __| '__/ _ \/ _ \ '_ \ 
| | | | (_| | |_) | | |_| |_\ \ | |  __/  __/ | | |
\_| |_/\__,_|_.__/|_|\__|\____/_|  \___|\___|_| |_|
""")
        print(Fore.YELLOW + Style.BRIGHT + f"Bem-vindo, {usuario_logado['nome']}! O que deseja fazer?")

        print(Fore.CYAN + """
╔═════════════════════════════════════════════════════════════════╗
║                          Menu Principal                         ║
║                                                                 ║
║ [1] Registrar Consumo                                           ║
║ [2] Ver Relatório                                               ║
║ [3] Ver Histórico                                               ║
║ [4] Editar ou Excluir Registro                                  ║
║ [5] Perfil                                                      ║
║ [0] Sair                                                        ║
╚═════════════════════════════════════════════════════════════════╝
""")

        opcao = input(Fore.CYAN + "→ Escolha uma opção: " + Style.RESET_ALL).strip()

        if opcao == "1":
            from registro import registro
            registro()
        elif opcao == "2":
            from relatorio import relatorio_do_dia
            relatorio_do_dia()
        elif opcao == "3":
            from historico import ver_historico
            ver_historico()
        elif opcao == "4":
            from editar_excluir import editar_ou_excluir
            editar_ou_excluir()
        elif opcao == "5":
            from perfil import perfil_usuario
            perfil_usuario(usuario_logado["id"])
        elif opcao == "0":
            from tela_boas_vindas import tela_boas_vindas
            print(Fore.CYAN + "\nAté logo! Retornando à tela inicial...")
            input("Pressione Enter para continuar...")
            tela_boas_vindas()
            break
        else:
            print(Fore.RED + "\nOpção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
>>>>>>> feature/pedro
