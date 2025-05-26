# Este arquivo é responsável por armazenar os dados do usuário logado durante a sessão do sistema.
# Ele funciona como uma "memória temporária" enquanto o programa está em execução,
# permitindo que diferentes partes do sistema acessem as informações do usuário autenticado.

# Dicionário global que armazena os dados do usuário atualmente logado.
# As chaves representam os campos principais de identificação do usuário.
usuario_logado = {
    "id": None,      # Armazena o ID único do usuário no banco de dados. Inicialmente None (nenhum usuário logado).
    "nome": None,    # Armazena o nome do usuário. Inicialmente None.
    "email": None    # Armazena o e-mail do usuário. Inicialmente None.
}

# Observações de boas práticas:
# - O uso de um dicionário global facilita o compartilhamento das informações do usuário entre diferentes módulos do sistema.
# - Os valores são definidos como None até que o login seja realizado, evitando dados residuais de sessões anteriores.
# - Não armazene informações sensíveis como senhas neste dicionário, por questões de segurança.
# - Ao fazer logout, é recomendável redefinir todos os valores para None.
