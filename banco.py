import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="database-fa"
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, values=None):
        """Executa um comando SQL."""
        self.cursor.execute(query, values or ())
        self.conn.commit()

    def fetchone(self, query, values=None):
        """Busca um único resultado no banco de dados."""
        self.cursor.execute(query, values or ())
        return self.cursor.fetchone()

    def fetchall(self, query, values=None):
        """Busca todos os resultados de uma query."""
        self.cursor.execute(query, values or ())
        return self.cursor.fetchall()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.cursor.close()
        self.conn.close()
