from colorama import Fore, Style, init
from banco import Database
import os
from tela_boas_vindas import tela_boas_vindas


init(autoreset=True)  # Iniciar colorama


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

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
┌───────────────┐
│ Opções:       │
│               │
│ [1] Login     │
│ [2] Cadastrar │
│ [3] Sair      │
└───────────────┘
"""
