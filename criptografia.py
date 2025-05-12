import numpy as np
from sympy import Matrix

# Matriz de chave para a Cifra de Hill
CHAVE_HILL = [[6,  24, 1], 
              [13, 16, 10],
              [20, 17, 15]]

# Alfabeto personalizado com letras, números e caracteres especiais
ALFABETO = "🐻ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~ "

# Função para obter o índice de um caractere no alfabeto
def char_to_index(char):
    return ALFABETO.index(char)

# Função para obter o caractere correspondente a um índice no alfabeto
def index_to_char(index):
    return ALFABETO[index % len(ALFABETO)]



# Função para criptografar usando a Cifra de Hill
def cifra_hill_criptografar(texto, chave):
    texto = texto.replace(" ", "")  # Remove espaços
    while len(texto) % len(chave) != 0:  # Preenche com o primeiro caractere do alfabeto para completar o bloco
        texto += ALFABETO[0]

    matriz_texto = [char_to_index(char) for char in texto]
    matriz_texto = np.array(matriz_texto).reshape(-1, len(chave))

    matriz_chave = np.array(chave)
    criptografado = (np.dot(matriz_texto, matriz_chave) % len(ALFABETO)).flatten()

    return ''.join(index_to_char(int(num)) for num in criptografado)



# Função para descriptografar usando a Cifra de Hill
def cifra_hill_descriptografar(texto, chave):
    matriz_texto = [char_to_index(char) for char in texto]
    matriz_texto = np.array(matriz_texto).reshape(-1, len(chave))

    # Calcula a inversa modular da matriz chave usando SymPy
    matriz_chave = Matrix(chave)
    matriz_chave_inversa = matriz_chave.inv_mod(len(ALFABETO))
    matriz_chave_inversa = np.array(matriz_chave_inversa).astype(int)

    descriptografado = (np.dot(matriz_texto, matriz_chave_inversa) % len(ALFABETO)).flatten()
    return ''.join(index_to_char(int(num)) for num in descriptografado)



# Testando a função corrigida
texto_original = "senha123@@@@%%%@1"
texto_criptografado = cifra_hill_criptografar(texto_original, CHAVE_HILL)
texto_descriptografado = cifra_hill_descriptografar(texto_criptografado, CHAVE_HILL)

print(f"Texto original: {texto_original}")
print(f"Texto criptografado: {texto_criptografado}")
print(f"Texto descriptografado: {texto_descriptografado}")