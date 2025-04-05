from banco import Database
from colorama import init, Fore, Style
from tela_boas_vindas import tela_boas_vindas
import os

#se esta 
is_checked = False

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    limpar_tela()
    titulo_ascii = Fore.CYAN + Style.BRIGHT +"""
  _                        _         
 | |                      (_)        
 | |        ___     __ _   _   _ __  
 | |       / _ \   / _` | | | | '_ \ 
 | |____  | (_) | | (_| | | | | | | |
 |______|  \___/   \__, | |_| |_| |_|
                    __/ |            
                   |___/                         
    """
    
    menu_lateral = Fore.YELLOW + """
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Digite [0] para voltar ao menu                                         │
 └────────────────────────────────────────────────────────────────────────┘
"""
    print(titulo_ascii,menu_lateral)
    
    #quando o usuario não digitar o email e senha corretos, o loop continua
    while not is_checked:
      email=input("Digite seu email: \t")
      if email == "0":
          tela_boas_vindas()
          return
      senha=input("Digite sua senha: \t")
      if senha == "0":
          tela_boas_vindas()
          return
      
      #verificar login
      check_login(email, senha)

#função para verificar se o email e senha estão corretos
def check_login(email, senha):

  #abrir o banco de dados
  db = Database()

  #query
  user = db.fetchone("SELECT * FROM tb_client WHERE cli_email = %s AND cli_password = %s", (email, senha))
  db.close()

  if user:
      #se o email e senha estiverem corretos, is_checked será True
      is_checked = True
      input(Fore.GREEN + "\n✅ E-mail válido. Acesso permitido.\n")
      input(Fore.CYAN + "Pressione [Enter] para continuar...")
      menu()
  else:
      print(Fore.RED + "\n❌ E-mail inválido. Tente novamente.\n")

   