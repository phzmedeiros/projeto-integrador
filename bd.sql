-- Criação do banco de dados com nome 'database-fa'
-- Este comando cria um novo banco de dados chamado 'database-fa' caso ele ainda não exista.
-- O nome entre crases permite o uso de hífen, que normalmente não é aceito em nomes de banco.
CREATE DATABASE IF NOT EXISTS `database-fa`;

-- Define que todas as operações a seguir serão feitas nesse banco
-- O comando USE seleciona o banco de dados 'database-fa' para que os próximos comandos SQL sejam executados nele.
USE `database-fa`;

-- Criação da tabela de clientes (usuários do sistema)
CREATE TABLE tb_client (
    cli_id INT AUTO_INCREMENT PRIMARY KEY,      -- Identificador único do cliente (gerado automaticamente pelo banco)
    cli_name VARCHAR(50) NOT NULL,              -- Nome do usuário, até 50 caracteres (campo obrigatório)
    cli_email VARCHAR(50) NOT NULL UNIQUE,      -- E-mail do usuário, até 50 caracteres, deve ser único (não pode repetir)
    cli_password VARCHAR(50) NOT NULL,          -- Senha do usuário (armazenada como texto, recomendável criptografar em produção)
    cli_cpf VARCHAR(50) NOT NULL UNIQUE         -- CPF do usuário, até 50 caracteres, deve ser único (não pode repetir)
);

-- Criação da tabela onde ficam armazenados os registros diários de sustentabilidade
CREATE TABLE tb_register (
    id INT NOT NULL AUTO_INCREMENT,             -- ID do registro diário, gerado automaticamente (chave primária)
    user_id INT NOT NULL,                       -- ID do usuário que fez o registro (referência à tabela tb_client)
    date DATE NOT NULL,                         -- Data do registro (formato: AAAA-MM-DD)
    water FLOAT NOT NULL,                       -- Consumo de água em litros (campo obrigatório)
    energy FLOAT NOT NULL,                      -- Consumo de energia em kWh (campo obrigatório)
    organic_waste FLOAT NOT NULL,               -- Quantidade de lixo orgânico produzido em kg (campo obrigatório)
    recyclable_waste FLOAT NOT NULL,            -- Quantidade de lixo reciclável produzido em kg (campo obrigatório)
    transport VARCHAR(45) NOT NULL,             -- Tipo de transporte utilizado no dia (até 45 caracteres)
    PRIMARY KEY (id),                           -- Define o campo 'id' como chave primária da tabela
    FOREIGN KEY (user_id) REFERENCES tb_client(cli_id) -- Cria uma chave estrangeira ligando o registro ao usuário correspondente
);

-- Inserção de um usuário administrador padrão no sistema
-- Este comando insere um usuário chamado 'admin' com e-mail, senha e CPF definidos.
-- A senha está em texto puro (NÃO recomendado em produção, apenas para testes iniciais).
INSERT INTO tb_client (cli_name, cli_email, cli_password, cli_cpf)
VALUES ('admin', 'admin@email.com', 'admin123', '00000000000');