# Importa a função 'tela_boas_vindas' do módulo 'tela_boas_vindas'.
# Essa função é responsável por exibir a tela inicial do sistema, geralmente com um menu de opções para o usuário.
from tela_boas_vindas import tela_boas_vindas

# O bloco abaixo verifica se este arquivo está sendo executado diretamente pelo Python.
# Isso é uma boa prática em Python para garantir que certos trechos de código só sejam executados
# quando o arquivo for o ponto de entrada principal do programa, e não quando for importado como módulo por outro arquivo.
if __name__ == "__main__":
    # Chama a função 'tela_boas_vindas', que inicia a interface do usuário.
    # A partir daqui, o usuário verá o menu inicial e poderá navegar pelo sistema.
    tela_boas_vindas()
