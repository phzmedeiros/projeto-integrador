import numpy as np
from sympy import Matrix

# Matriz de chave 
CHAVE = [[6,  24, 1 ], 
        [13, 16, 10],
        [20, 17, 15]]


chave_invertida = np.linalg.inv(CHAVE)
 
print(chave_invertida)


# Alfabeto personalizado com letras, números e caracteres especiais
ALFABETO = "🐻ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~ "

# Função para obter o índice de um caractere no alfabeto
def char_to_index(char):
    return ALFABETO.index(char)

# Função para obter o caractere correspondente a um índice no alfabeto
def index_to_char(index):
    return ALFABETO[index % len(ALFABETO)]


# Função para criptografar 
def criptografar(texto, chave):
    while len(texto) % len(chave) != 0:  # Preenche com o primeiro caractere do alfabeto para completar o bloco
        texto += ALFABETO[0]

    matriz_texto = [char_to_index(char) for char in texto]
    matriz_texto = np.array(matriz_texto).reshape(-1, len(chave))

    matriz_chave = np.array(chave)

    criptografado = (np.dot(matriz_texto, matriz_chave)).flatten()

    
    return criptografado


# Função para descriptografar 
def descriptografar(matriz, chave):
    #multiplicação da matriz criptografada pela inversa da matriz chave
    matriz = np.array(matriz).reshape(-1, len(chave))


    # Calcular a inversa da matriz chave
    matriz_chave = np.array(chave)
    matriz_chave = Matrix(matriz_chave)
    inversa_chave = matriz_chave.inv()

    # Descriptografar
    descriptografado = (np.dot(matriz, inversa_chave)).flatten()
    # Remover o preenchimento
    for i in range(len(descriptografado)):
        if descriptografado[i] == char_to_index(ALFABETO[0]):
            descriptografado = descriptografado[:i]
            break

    return ''.join(index_to_char(int(num)) for num in descriptografado)
    

#testando 
if __name__ == "__main__":
    texto = "73537 cr1pt0gr@f4d0"
    print("Texto original:", texto)
    
    # Criptografar
    criptografado = criptografar(texto, CHAVE)
    print("Texto criptografado:", criptografado)
    
    # Descriptografar
    descriptografado = descriptografar(criptografado, CHAVE)
    print("Texto descriptografado:", descriptografado)