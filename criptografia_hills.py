import numpy as np  # Importa a biblioteca NumPy para operações matriciais
from sympy import Matrix  # Importa a biblioteca SymPy para trabalhar com álgebra simbólica

# Esta é a matriz usada como chave para criptografar e descriptografar o texto.
# A Cifra de Hill exige que seja uma matriz quadrada (n x n), neste caso, 3x3.
CHAVE_HILL = [
    [2, 4, 5],
    [9, 2, 1],
    [3, 17, 7]
]

# Este é o alfabeto que será utilizado na criptografia.
# Inclui letras, números e caracteres especiais. O primeiro caractere (🐻) é usado como preenchimento (padding).
# O tamanho total do alfabeto (94 caracteres) será utilizado como módulo nas operações matemáticas.
ALFABETO = r"🐻ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~ "

# Esta função localiza a posição (índice) de um caractere dentro do alfabeto personalizado.
def char_to_index(char):
    return ALFABETO.index(char)  # Retorna o número correspondente ao caractere

# Esta função faz o inverso da anterior: dado um índice, retorna o caractere correspondente no alfabeto.
def index_to_char(index):
    return ALFABETO[index % len(ALFABETO)]  # Aplica módulo para evitar erros de índice

# Função responsável por criptografar uma mensagem de texto usando a Cifra de Hill
def cifra_hill_criptografar(texto, chave):
    # Enquanto o texto não for múltiplo do tamanho da matriz (3), adiciona o caractere de padding (🐻)
    while len(texto) % len(chave) != 0:
        texto += ALFABETO[0]  # Adiciona o caractere de preenchimento

    # Converte cada caractere do texto em um número baseado na posição no alfabeto
    matriz_texto = [char_to_index(char) for char in texto]
    # Agrupa os números em blocos de 3 colunas (para multiplicar com matriz 3x3)
    matriz_texto = np.array(matriz_texto).reshape(-1, len(chave))

    # Converte a chave para uma matriz NumPy
    matriz_chave = np.array(chave)

    # Multiplica cada bloco de texto pela matriz chave e aplica módulo do tamanho do alfabeto
    criptografado = (np.dot(matriz_texto, matriz_chave) % len(ALFABETO)).flatten()

    # Converte os números de volta para caracteres para formar o texto criptografado final
    return ''.join(index_to_char(int(num)) for num in criptografado)

# Função responsável por descriptografar o texto criptografado
def cifra_hill_descriptografar(texto, chave):
    # Converte os caracteres criptografados de volta para números
    matriz_texto = [char_to_index(char) for char in texto]
    matriz_texto = np.array(matriz_texto).reshape(-1, len(chave))  # Agrupa em blocos

    # Converte a matriz chave original para um objeto simbólico do SymPy
    matriz_chave = Matrix(chave)

    # Calcula a inversa da matriz chave, mas no sistema modular (mod 94)
    inversa_chave = matriz_chave.inv_mod(len(ALFABETO))  # Inversa no módulo
    inversa_chave = np.array(inversa_chave).astype(int) % len(ALFABETO)  # Conversão para NumPy

    # Calcula a inversa real da matriz, usada apenas para fins de debug
    inversa_chave_nao_mod = matriz_chave.inv()

    # Se a variável DEBUG for True, imprime a inversa real da matriz (apenas para testes internos)
    DEBUG = False
    if DEBUG:
        print("matriz chave vezes a inversa", np.dot(matriz_chave, inversa_chave_nao_mod))
        print("Inversa não mod:", inversa_chave_nao_mod)

    # Realiza a multiplicação da matriz de texto pela inversa da chave e aplica módulo do alfabeto
    descriptografado = (np.dot(matriz_texto, inversa_chave) % len(ALFABETO)).flatten()

    # Remove o caractere de preenchimento (🐻), que foi adicionado na criptografia
    for i in range(len(descriptografado)):
        if descriptografado[i] == char_to_index(ALFABETO[0]):  # Verifica se é o caractere de padding
            descriptografado = descriptografado[:i]  # Remove a partir dele
            break

    # Converte os números de volta para caracteres normais
    return ''.join(index_to_char(int(num)) for num in descriptografado)

# Bloco principal de teste do sistema: é executado apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    texto = "73537 cr1pt0gr@f4d0"  # Exemplo de texto para ser criptografado
    print("Texto original:", texto)

    # Criptografa o texto
    criptografado = cifra_hill_criptografar(texto, CHAVE_HILL)
    print("Texto criptografado:", criptografado)

    # Descriptografa o texto
    descriptografado = cifra_hill_descriptografar(criptografado, CHAVE_HILL)
    print("Texto descriptografado:", descriptografado)
