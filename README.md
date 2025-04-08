# 🌱 HabitGreen – Sistema de Monitoramento de Sustentabilidade Pessoal

**HabitGreen** é um sistema acadêmico desenvolvido por estudantes de Engenharia de Software da **Pontifícia Universidade Católica de Campinas (PUC-Campinas)**, como parte do componente curricular **Projeto Integrador I – 1º Semestre**.

O sistema tem como objetivo **estimular hábitos sustentáveis no cotidiano das pessoas** por meio de um terminal interativo em Python, permitindo o registro diário do consumo de água, energia, resíduos e transporte. Ao final de cada registro, o sistema fornece análises visuais, pontuações e mensagens educativas de um mascote em ASCII – o **urso polar**, símbolo da conscientização ambiental.

---

## 🎓 Contexto Acadêmico

Este projeto integra os conhecimentos adquiridos ao longo do semestre nas disciplinas de:

- **Lógica de Programação**
- **Fundamentos de Banco de Dados**
- **Projeto Integrador**
- **Tecnologias em TI**

Além de aplicar práticas de **controle de versão com Git**, **trabalho em equipe** e **planejamento com metodologia ágil**, promovendo uma vivência real de desenvolvimento de software.

---

## 🧠 Objetivos do Projeto

- Desenvolver um sistema funcional e educativo executado em terminal (CLI)
- Estimular a reflexão e melhoria dos hábitos de sustentabilidade
- Aplicar boas práticas de programação e organização de código
- Utilizar banco de dados real (MySQL) com estrutura relacional
- Promover visualização clara com gráficos ASCII e feedback instantâneo

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **MySQL**
- **Colorama** – para cores no terminal
- **Termgraph** – gráficos ASCII de barras
- **Git e GitHub** – versionamento colaborativo
- **ASCII Art** – mascote educativo (urso polar)

---

## 👥 Equipe Acadêmica

| Nome     | Função Principal                | Branch Git                         |
|----------|----------------------------------|------------------------------------|
| Alinne   | Desenvolvimento próprio.            | `feature/alinne`                |
| Alycia   | Desenvolvimento próprio.       | `feature/alycia`                |
| Pedro    | Desenvolvimento próprio.     | `feature/pedro`          |
| Rafael   | Desenvolvimento próprio.    | `feature/rafael`         |

---

## 📁 Estrutura do Projeto

/habitgreen <br>
│ <br>
├── main.py <br>
├── tela_boas_vindas.py <br>
├── login.py <br>
├── cadastro.py <br>
├── menu.py <br>
├── registro.py <br>
├── relatorio.py <br>
├── historico.py <br>
├── editar_excluir.py <br>
├── urso_polar_ascii.py <br>
├── banco.py <br>
├── utils.py <br>
└── requirements.txt

---

## 🔄 Estrutura de Branches Git

main ← versão final e estável <br>
└── develop ← integração de funcionalidades <br>
----├── feature/alinne-ui <br>
----├── feature/alycia-db <br>
----├── feature/pedro-registros <br>
----└── feature/rafael-relatorio

---

## 🚀 Instruções de Execução

1. Clone o repositório:
git clone https://github.com/seu-usuario/habitgreen.git

2. Instale os pacotes necessários:
pip install -r requirements.txt

3. Configure o banco de dados MySQL com o script SQL fornecido

4. Execute o sistema:
python main.py

---

## 🐻‍❄️ Sobre o Mascote

O **urso polar ASCII** representa o impacto das ações humanas nas mudanças climáticas. Ele interage com o usuário após cada análise, oferecendo mensagens motivacionais e dicas personalizadas baseadas na pontuação do dia.

---

## 📚 Licença e Uso

Este projeto é de caráter **estritamente acadêmico**. Todos os direitos reservados à equipe desenvolvedora. O uso e redistribuição devem respeitar o contexto educacional para o qual o projeto foi criado.

---

> Projeto Integrador I – 1º Semestre  
> **PUC Campinas – Engenharia de Software**  
> 2025
