import numpy as np
from sympy import Matrix

# Matriz de chave para a Cifra de Hill
CHAVE_HILL = [
    [2, 4, 5],
    [9, 2, 1],
    [3, 17, 7]
]

# Alfabeto personalizado com letras, números e caracteres especiais
#modulo 94
ALFABETO = r"🐻ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~ "


# Função para obter o índice de um caractere no alfabeto
def char_to_index(char):
    return ALFABETO.index(char)

# Função para obter o caractere correspondente a um índice no alfabeto
def index_to_char(index):
    return ALFABETO[index % len(ALFABETO)]


# Função para criptografar usando a Cifra de Hill
def cifra_hill_criptografar(texto, chave):
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

    # Calcular a inversa da matriz chave
    matriz_chave = np.array(chave)
    matriz_chave = Matrix(matriz_chave)
    inversa_chave = matriz_chave.inv_mod(len(ALFABETO))
    inversa_chave = np.array(inversa_chave).astype(int)
    inversa_chave = inversa_chave % len(ALFABETO)

    
    inversa_chave_nao_mod = matriz_chave.inv()
    DEBUG = False  # ou True para ambiente de teste

    if DEBUG:
        print("matriz chave vezes a inversa", np.dot(matriz_chave, inversa_chave_nao_mod))
        print("Inversa não mod:", inversa_chave_nao_mod)

        print("matriz chave vezes a inversa",np.dot(matriz_chave, inversa_chave_nao_mod))
    
        print("Inversa não mod:", inversa_chave_nao_mod)

    # Descriptografar
    descriptografado = (np.dot(matriz_texto, inversa_chave) % len(ALFABETO)).flatten()
    # Remover o preenchimento
    for i in range(len(descriptografado)):
        if descriptografado[i] == char_to_index(ALFABETO[0]):
            descriptografado = descriptografado[:i]
            break

    return ''.join(index_to_char(int(num)) for num in descriptografado)
    

#testando a cifra de Hill
if __name__ == "__main__":
    texto = "73537 cr1pt0gr@f4d0"
    print("Texto original:", texto)
    
    # Criptografar
    criptografado = cifra_hill_criptografar(texto, CHAVE_HILL)
    print("Texto criptografado:", criptografado)
    
    # Descriptografar
    descriptografado = cifra_hill_descriptografar(criptografado, CHAVE_HILL)
    print("Texto descriptografado:", descriptografado)