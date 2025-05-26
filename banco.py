# Importa a biblioteca mysql.connector, que permite ao Python se conectar e interagir com bancos de dados MySQL.
import mysql.connector

# Define uma classe chamada Database, que será responsável por todas as operações com o banco de dados.
class Database:
    # Método construtor da classe. É chamado automaticamente quando criamos um novo objeto Database.
    def __init__(self):
        # self.conn armazena a conexão ativa com o banco de dados MySQL.
        # Aqui são passados os parâmetros necessários para conectar:
        self.conn = mysql.connector.connect(
            host="localhost",        # Endereço do servidor do banco de dados. 'localhost' significa o próprio computador.
            port=3306,               # Porta padrão do MySQL. Normalmente é 3306.
            user="root",             # Nome de usuário do MySQL. 'root' é o administrador padrão.
            password="",             # Senha do usuário. Aqui está vazia, mas em produção deve ser uma senha forte.
            database="database-fa"   # Nome do banco de dados que será utilizado. Deve existir previamente no MySQL.
        )

        # self.cursor cria um objeto cursor, que serve para executar comandos SQL e navegar pelos resultados.
        self.cursor = self.conn.cursor()

    # Método para executar comandos SQL que modificam dados (INSERT, UPDATE, DELETE).
    # query: string com o comando SQL.
    # values: tupla com os valores a serem inseridos nos espaços (%s) do SQL.
    def execute(self, query, values=None):
        """
        Executa um comando SQL no banco. Por exemplo:
        - Inserir um novo usuário
        - Atualizar dados
        - Deletar registros
        """
        # Executa o comando SQL passado em 'query', usando os valores fornecidos (ou tupla vazia se não houver).
        self.cursor.execute(query, values or ())

        # commit() confirma as alterações feitas no banco de dados.
        # Sem esse comando, as mudanças não seriam salvas permanentemente.
        self.conn.commit()

    # Método para buscar apenas UM resultado do banco de dados (SELECT).
    # query: string com o comando SQL.
    # values: tupla com os valores para o SQL.
    def fetchone(self, query, values=None):
        """
        Executa uma consulta SQL (SELECT) e retorna apenas um resultado (o primeiro).
        Ideal para verificar dados únicos como login ou CPF.
        """
        # Executa o comando SELECT com os valores fornecidos (ou tupla vazia).
        self.cursor.execute(query, values or ())

        # Retorna a primeira linha encontrada pelo banco de dados.
        # Se não houver resultado, retorna None.
        return self.cursor.fetchone()

    # Método para buscar TODOS os resultados de uma consulta SQL (SELECT).
    # query: string com o comando SQL.
    # values: tupla com os valores para o SQL.
    def fetchall(self, query, values=None):
        """
        Executa uma consulta SQL (SELECT) e retorna todos os resultados encontrados.
        Ideal para quando precisamos mostrar uma lista completa, como:
        - Todos os registros de um usuário
        - Todas as datas cadastradas
        """
        # Executa o comando SELECT com os valores fornecidos (ou tupla vazia).
        self.cursor.execute(query, values or ())

    # Método para fechar a conexão com o banco de dados.
    # Muito importante para liberar os recursos da memória e encerrar conexões abertas.
    def close(self):
        """
        Fecha a conexão com o banco de dados.
        Deve ser chamado sempre que terminar de usar a conexão para evitar problemas de desempenho ou bloqueios no MySQL.
        """
        self.cursor.close()  # Encerra o cursor
        self.conn.close()    # Encerra a conexão com o banco
