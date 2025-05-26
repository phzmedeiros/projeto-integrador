# Importa a biblioteca NumPy, usada para cálculos com vetores e matrizes
import numpy as np

# Importa o SymPy, usado aqui para calcular a inversa da matriz (reversão da criptografia)
from sympy import Matrix

# Define a matriz CHAVE que será usada para criptografar e descriptografar o texto.
# Esta matriz precisa ser invertível (ou seja, ter uma inversa válida) para que a descriptografia funcione.
CHAVE = [[6, 24, 1],
         [13, 16, 10],
         [20, 17, 15]]

# Calcula a inversa REAL da matriz (não é a inversa modular)
# Isso é usado aqui apenas como visualização ou teste matemático
chave_invertida = np.linalg.inv(CHAVE)
print(chave_invertida)

# Alfabeto personalizado com letras, números e símbolos
# Inclui o emoji 🐻 no início, usado como caractere de preenchimento (padding)
ALFABETO = "🐻ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~ "

# Esta função retorna o número (índice) correspondente a um caractere no alfabeto
# Ex: 'A' → 1, 'a' → 27, '@' → 65...
def char_to_index(char):
    return ALFABETO.index(char)

# Esta função faz o contrário da anterior: converte um número em caractere, respeitando o alfabeto
# Usa módulo (%) para garantir que o índice sempre esteja dentro do tamanho do alfabeto
def index_to_char(index):
    return ALFABETO[index % len(ALFABETO)]

# Esta função criptografa um texto usando a Cifra de Hill (multiplicação de vetores por matriz)
def criptografar(texto, chave):
    # Verifica se o texto tem tamanho múltiplo de 3. Se não tiver, adiciona o 🐻 até completar.
    while len(texto) % len(chave) != 0:
        texto += ALFABETO[0]  # Adiciona 🐻 para preencher o bloco

    # Converte cada caractere do texto em seu índice no alfabeto
    matriz_texto = [char_to_index(char) for char in texto]
    # Agrupa os números em blocos de 3 colunas, para multiplicação com matriz 3x3
    matriz_texto = np.array(matriz_texto).reshape(-1, len(chave))

    # Converte a lista da chave para matriz NumPy
    matriz_chave = np.array(chave)

    # Multiplica os blocos do texto pela matriz chave (criptografia)
    # Obs: ainda sem aplicar módulo — para fins didáticos/matemáticos
    criptografado = (np.dot(matriz_texto, matriz_chave)).flatten()

    # Retorna o vetor criptografado (números inteiros, ainda não convertidos para texto)
    return criptografado

# Esta função descriptografa a matriz numérica obtida na criptografia
def descriptografar(matriz, chave):
    # Converte a lista de números criptografados em blocos de 3 colunas
    matriz = np.array(matriz).reshape(-1, len(chave))

    # Converte a chave para matriz simbólica do SymPy para conseguir calcular a inversa real
    matriz_chave = np.array(chave)
    matriz_chave = Matrix(matriz_chave)

    # Calcula a inversa REAL da matriz (não modular)
    inversa_chave = matriz_chave.inv()

    # Multiplica a matriz criptografada pela inversa da chave para descriptografar
    descriptografado = (np.dot(matriz, inversa_chave)).flatten()

    # Remove o caractere de padding (🐻) se ele foi adicionado no final
    for i in range(len(descriptografado)):
        if descriptografado[i] == char_to_index(ALFABETO[0]):
            descriptografado = descriptografado[:i]
            break

    # Converte os números descriptografados de volta para texto
    return ''.join(index_to_char(int(num)) for num in descriptografado)

# Bloco que será executado quando este arquivo for rodado diretamente
# Aqui é feita uma simulação para testar o funcionamento da criptografia e descriptografia
if __name__ == "__main__":
    texto = "73537 cr1pt0gr@f4d0"  # Exemplo de texto a ser criptografado
    print("Texto original:", texto)

    # Criptografa o texto
    criptografado = criptografar(texto, CHAVE)
    print("Texto criptografado:", criptografado)

    # Descriptografa o vetor de números gerado
    descriptografado = descriptografar(criptografado, CHAVE)
    print("Texto descriptografado:", descriptografado)
