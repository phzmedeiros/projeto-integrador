import os
import re
from colorama import init, Fore, Style

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_impacto(transporte_lista,distancia):
    impacto_dict = {
        "1": 0.02, # Bicicleta
        "2": 0.01, #Caminhada
        "3": 0.1, #Transporte Públic
        "4": 0.7, #Carro Elétrico
        "5": 0.8, #Carona Compartilhada
        "6": 1.5, #Carro a Combustível Fóssil
        "7": 2.0 #Caminhão/Avião
    }
    while True:
        impacto_total = 0
        try:
            for t in transporte_lista:
                t = str(t).strip()
                if t in impacto_dict:
                    impacto_total += distancia * impacto_dict[t]
                else:
                    raise ValueError (f"Transporte inválido: {t}. Use apenas opções de 1 a 7.")
            return impacto_total
        except ValueError as e:
            print(e)
            transporte = input ("\nDigite novamente os meios de transporte válidos (de 1 a 7), separados por vírgula: ")
            transporte_lista = transporte.split(",")


def classificar_transporte(transporte_lista):
    sustentaveis = {"1", "2", "3"}
    nao_sustentaveis = {"6", "7"}

    if all(t in sustentaveis for t in transporte_lista):
        return "Sustentável"
    elif any(t in sustentaveis for t in transporte_lista) and any(t in nao_sustentaveis):
        return "Misto"
    else:
        return "Não Sustentável"
    
def validar_data():
    while True:
      data = input(Fore.BLUE + "📅 Digite a data (DD-MM-AAAA):")
      if re.match(r"^\d{2}-\d{2}-\d{4}$", data):
        return data
      print(Fore.YELLOW + "❌ Formato inválido! Use DD-MM-AAAA.")

def validar_numero(mensagem):
    while True:
        try:
            valor = float(input(Fore.BLUE + mensagem))
            if valor >=0:
                return valor
            else:
                 print(Fore.YELLOW + "❌ O valor não pode ser negativo.")
        except ValueError:
           print(Fore.YELLOW + "❌ Entrada inválida! Digite um número.")

def validar_transporte():
    while True:
        transporte = input(Fore.YELLOW + "Digite os números correspondentes separados por vírgula. (Ex: 1,3): ")
        transporte_lista = transporte.split(",")
        if all (t.strip().isdigit() and 1 <= int(t.strip()) <=7 for t in transporte_lista):
            return [t.strip() for t in transporte_lista]
        print (Fore.YELLOW + "❌ Entrada inválida! Escolha números de 1 a 7, separados por vírgula.")

def classificar_sustentabilidade(valor, limite_baixo, limite_medio):
        if valor <= limite_baixo:
            return "Alta Sustentabilidade"
        elif valor <= limite_medio:
            return "Média Sustentabilidade"
        else:
            return "Baixa Sustentabilidade"

def registrar_dados():
    limpar_tela()
    print(Fore.GREEN + Style.BRIGHT + """
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
""")

    print(Fore.CYAN + "┌───────────────────────────────────────────────────────────────┐")

    data = validar_data()
    agua = validar_numero("💧 Água consumida (litros): ")
    energia = validar_numero("⚡ Energia consumida (kWh): ")
    residuos_nao_reciclaveis = validar_numero("🗑️ Resíduos não recicláveis (kg): ")
    residuos_reciclados = validar_numero("♻️ Resíduos reciclados (%): ")
    
    print(Fore.YELLOW + "\n🚗 Escolha os meios de transporte usados no dia:")
    print(Fore.WHITE + "+------------------------------------+")
    print(Fore.WHITE + "|  1 - Bicicleta 🚴                  |")
    print(Fore.WHITE + "|  2 - Caminhada 🚶                  |")
    print(Fore.WHITE + "|  3 - Transporte Público 🚌         |")
    print(Fore.WHITE + "|  4 - Carro Elétrico ⚡🚗           |")
    print(Fore.WHITE + "|  5 - Carona Compartilhada 🚘       |")
    print(Fore.WHITE + "|  6 - Carro a Combustível Fóssil 🚗 |")
    print(Fore.WHITE + "|  7 - Caminhão/Avião ✈️🚛            |")
    print(Fore.WHITE + "+------------------------------------+")

    transporte_lista = validar_transporte()
    distancia = validar_numero ("📏 Distância total percorrida (km): ")
    impacto_transporte = calcular_impacto(transporte_lista, distancia)
    categoria_transporte = classificar_transporte(transporte_lista)
        
    sustentabilidade_agua = classificar_sustentabilidade(agua, 150, 300)
    sustentabilidade_energia = classificar_sustentabilidade(energia, 5, 15)
    sustentabilidade_residuos = classificar_sustentabilidade(residuos_nao_reciclaveis, 1, 3)
    sustentabilidade_transporte = classificar_sustentabilidade (impacto_transporte, 1, 3)

    print(Fore.GREEN + f"\n💧 Sustentabilidade da Água: {sustentabilidade_agua}")
    print(Fore.GREEN + f"⚡ Sustentabilidade da Energia: {sustentabilidade_energia}")
    print(Fore.GREEN + f"🗑️ Sustentabilidade dos Resíduos: {sustentabilidade_residuos}")
    print(Fore.GREEN + f"🚗 Sustentabilidade do Transporte: {sustentabilidade_transporte}")
    
    dados = f"{data}, {agua}, {energia}, {residuos_nao_reciclaveis}, {residuos_reciclados}, {'/'.join(transporte_lista)}, {distancia}, {impacto_transporte}, {categoria_transporte}, {sustentabilidade_agua}, {sustentabilidade_energia}, {sustentabilidade_residuos}, {sustentabilidade_transporte}\n"

    with open("registro_sustentavel.txt", "a") as arquivo:
        arquivo.write(dados)

    print(Fore.GREEN + "\n✅ Dados registrados com sucesso! Vamos rumo a um mundo mais sustentável! 🌱")

if __name__ == "__main__":
    registrar_dados()