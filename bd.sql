CREATE DATABASE IF NOT EXISTS `database-fa`;
USE `database-fa`;

CREATE TABLE tb_client (
    cli_id INT AUTO_INCREMENT PRIMARY KEY,
    cli_name VARCHAR(50) NOT NULL,
    cli_email VARCHAR(50) NOT NULL UNIQUE,
    cli_password VARCHAR(50) NOT NULL,
    cli_cpf VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE tb_register (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    date DATE NOT NULL,
    water FLOAT NOT NULL,
    energy FLOAT NOT NULL,
    organic_waste FLOAT NOT NULL,
    recyclable_waste FLOAT NOT NULL,
    transport VARCHAR(45) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES tb_client(cli_id)
);

CREATE TABLE tb_score (
    id INT NOT NULL AUTO_INCREMENT,
    register_id INT NOT NULL,
    point_water INT NOT NULL,
    point_energy INT NOT NULL,
    point_waste INT NOT NULL,
    point_transport INT NOT NULL,
    point_geral INT NOT NULL,
    tip VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (register_id) REFERENCES tb_register(id)
);

INSERT INTO tb_client (cli_name, cli_email, cli_password, cli_cpf)
VALUES ('admin', 'admin@email.com', 'admin123', '00000000000');