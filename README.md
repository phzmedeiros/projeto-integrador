# 🌱 HabitGreen – Sistema de Monitoramento de Sustentabilidade Pessoal

**HabitGreen** é um sistema acadêmico completo desenvolvido por estudantes de Engenharia de Software da **Pontifícia Universidade Católica de Campinas (PUC-Campinas)**, no âmbito do componente curricular **Projeto Integrador I – 1º Semestre**.

O sistema tem como propósito **conscientizar o indivíduo sobre seu impacto ambiental**, oferecendo uma experiência interativa por terminal (CLI), com registro diário de consumo, análise automatizada e recomendações educativas através de um mascote em ASCII — o **Urso Polar**, símbolo da sustentabilidade.

---

## 🎯 Objetivos do Projeto

- Promover a mudança de hábitos sustentáveis por meio do autoconhecimento.
- Aplicar conceitos acadêmicos de programação, banco de dados e álgebra linear.
- Integrar disciplinas técnicas à prática com foco em usabilidade, segurança e modularização.
- Estimular o trabalho em equipe, versionamento e documentação profissional.

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- **MySQL** – banco relacional
- **Colorama** – estilização de terminal
- **ASCII Art** – mascote educativo (Urso Polar)
- **SymPy + NumPy** – criptografia (Cifra de Hill)
- **Git + GitHub** – controle de versão e colaboração

---

## 🎓 Contexto Acadêmico

Este projeto integra os conhecimentos adquiridos ao longo do semestre nas disciplinas de:

- **Lógica de Programação**
- **Fundamentos de Banco de Dados**
- **Projeto Integrador**
- **Tecnologias em TI**

Além de aplicar práticas de **controle de versão com Git**, **trabalho em equipe** e **planejamento com metodologia ágil**, promovendo uma vivência real de desenvolvimento de software.

---

## 🔍 Funcionalidades Principais

- ✅ **Cadastro/Login com criptografia de senha**
- 🧾 **Registro diário de:**
  - Consumo de água (litros)
  - Consumo de energia (kWh)
  - Lixo orgânico e reciclável (kg)
  - Tipo de transporte utilizado
- 📊 **Pontuação de sustentabilidade**
  - Classificação: Alta, Moderada ou Baixa
- 📈 **Relatórios com gráficos ASCII**
- 📚 **Histórico e evolução dos hábitos**
- ✏️ **Edição e exclusão de registros**
- 👤 **Perfil do usuário com médias gerais**
- 🔐 **Criptografia de senhas com Cifra de Hill**

---

## 🗃️ Estrutura de Diretórios

habitgreen/<br>
│<br>
├── main.py                 # Arquivo principal<br>
├── tela_boas_vindas.py     # Tela inicial<br>
├── cadastro.py             # Cadastro de usuários<br>
├── login.py                # Login e autenticação<br>
├── menu.py                 # Menu principal<br>
├── registro.py             # Registro de consumo<br>
├── relatorio.py            # Relatório diário<br>
├── historico.py            # Consulta de históricos<br>
├── editar_excluir.py       # Edição e exclusão<br>
├── perfil.py               # Perfil do usuário<br>
├── criptografia_hills.py   # Cifra de Hill<br>
├── banco.py                # Conexão com banco<br>
├── sessao.py               # Dados do usuário logado<br>
├── bd.sql                  # Script do banco de dados<br>
├── README.md               # Este documento

---

## 🧪 Estrutura de Testes

Cada funcionalidade foi validada com:

- Dados válidos e inválidos
- Prints do terminal e banco de dados
- Análise de retorno do sistema
- Comentários sobre os resultados

As funcionalidades testadas incluem: cadastro, login, registro de consumo, relatório, histórico, edição, exclusão, perfil e criptografia.

---

## 🧠 Fundamentação Matemática

O projeto integra conceitos de **Álgebra Linear** por meio da **Cifra de Hill**, usada para criptografar e descriptografar senhas. A implementação considera:

- Alfabeto personalizado (94 caracteres)
- Matrizes invertíveis modulares
- Padding para alinhamento dos blocos

---

## 🧵 Metodologia de Desenvolvimento

O projeto seguiu os princípios da **Aprendizagem Baseada em Projetos (PBL)** com foco em:

- Planejamento via Trello
- Versionamento no GitHub
- Programação em módulos
- Testes contínuos e documentados

---

## 👥 Equipe de Desenvolvimento

| Nome                                 |
|--------------------------------------|
| Alinne Monteiro de Melo              |
| Alycia Santos Bond                   |
| Pedro Henrique Medeiros dos Reis     |
| Rafael Antônio Candian               |

---

## 🚀 Como Rodar o Projeto
### Pré-requisitos

1. **Python 3.11 ou superior**
2. **MySQL 8.0+** instalado e configurado
3. As seguintes bibliotecas Python:
   - `colorama`
   - `numpy`
   - `sympy`
   - `mysql-connector-python`

### Instalação das bibliotecas:

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install colorama numpy sympy mysql-connector-python
```

### Configuração do banco:

- Abra o MySQL e execute o script `bd.sql` incluído no projeto para criar as tabelas necessárias.

### Execução do projeto:

```bash
python main.py
```

---

## 🐻 Sobre o Mascote

O **Urso Polar ASCII** é um personagem que orienta, motiva e comenta os resultados do dia, gerando um elo afetivo com o usuário e promovendo a educação ambiental de forma leve e lúdica.

---

## 🧠 Segurança

- As senhas são criptografadas usando Cifra de Hill com alfabeto personalizado. 
- O sistema não armazena senhas em texto puro.
- A descriptografia é feita apenas no momento da verificação durante o login.

---

## 🧪 Testes Implementados

- Todas as principais funcionalidades foram testadas com:
- Entradas válidas e inválidas
- Prints do terminal simulando o comportamento
- Confirmação de retorno esperado
- Prints do banco de dados

---

## ⚠️ Licença

Este projeto é de uso **exclusivamente acadêmico** e não deve ser utilizado para fins comerciais. Todos os direitos reservados à equipe desenvolvedora e à PUC-Campinas.

---

> Projeto Integrador I – 1º Semestre  
> Engenharia de Software – PUC Campinas – 2025
