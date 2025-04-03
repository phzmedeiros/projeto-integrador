from banco import Database
from colorama import init, Fore, Style
from tela_boas_vindas import tela_boas_vindas
import os

is_checked = False

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    limpar_tela()
    titulo_ascii = Fore.CYAN + Style.BRIGHT +"""
 _                _       
| |    ___   __ _(_)_ __  
| |   / _ \ / _` | | '_ \ 
| |__| (_) | (_| | | | | |
|_____\___/ \__, |_| |_|_|
            |___/                     
    """
    
    menu_lateral = Fore.YELLOW + """
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Digite [0] para voltar ao menu                                         │
 └────────────────────────────────────────────────────────────────────────┘
"""
    print(titulo_ascii,menu_lateral)
    

    while not is_checked:
      email=input("Digite seu email: \t")
      if email == "0":
          tela_boas_vindas()
          return
      senha=input("Digite sua senha: \t")
      if senha == "0":
          tela_boas_vindas()
          return
      check_login(email, senha)


def check_login(email, senha):

  db = Database()
  user = db.fetchone("SELECT * FROM tb_client WHERE cli_email = %s AND cli_password = %s", (email, senha))
  db.close()

  if user:
      is_checked = True
      print(Fore.GREEN + "\n✅ E-mail válido. Acesso permitido.\n")
  else:
      print(Fore.RED + "\n❌ E-mail inválido. Tente novamente.\n")

   