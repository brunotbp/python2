# 🐍 Python 2 - Módulo Django 🚀

Bem-vindo ao repositório de exercícios do módulo de **Django** do curso **Python 2**! Este espaço é dedicado à prática e ao aprofundamento dos conceitos aprendidos sobre o framework web Django.

---

## 📜 Sobre o Curso

O curso **Python 2** visa fornecer um conhecimento abrangente da linguagem Python, culminando no desenvolvimento de aplicações web robustas e escaláveis utilizando o framework Django. Este repositório contém os exercícios práticos referentes a este último módulo.

---

## 📂 Conteúdo do Repositório

Aqui você encontrará uma coleção de exercícios projetados para solidificar seu entendimento sobre os diversos aspectos do Django, incluindo:

* **Configuração de Ambiente e Projetos Django:** ⚙️
    * Instalação do Django e criação de projetos e apps.
    * Estrutura de um projeto Django.
* **Models e Banco de Dados:** 🗄️
    * Criação e gerenciamento de models.
    * Migrations e ORM do Django.
    * Consultas ao banco de dados.
* **Views e Templates:** 🖥️
    * Criação de views baseadas em funções e classes.
    * Utilização do sistema de templates do Django (DTL).
    * Passagem de contexto para templates.
* **Forms:** 📝
    * Criação e manipulação de formulários.
    * Validação de dados.
* **URLs e Roteamento:** 🔗
    * Definição de padrões de URL.
    * Roteamento de requisições para as views corretas.
* **Autenticação e Autorização:** 🔒
    * Implementação de sistemas de login e registro de usuários.
    * Gerenciamento de permissões.
* **Admin Interface:** 🛠️
    * Customização da interface administrativa do Django.
* **Testes:** ✔️
    * Criação de testes unitários e de integração.
* **Boas Práticas e Tópicos Avançados (conforme aplicável):** ✨
    * Organização de código.
    * Segurança.
    * Deployment (conceitos básicos).

---

## 🎯 Objetivos dos Exercícios

* Aplicar na prática os conceitos teóricos do Django.
* Desenvolver a capacidade de solucionar problemas comuns no desenvolvimento web com Django.
* Construir aplicações web funcionais e interativas.
* Familiarizar-se com o fluxo de desenvolvimento Django.

---

## ⚙️ Pré-requisitos

Antes de iniciar os exercícios, certifique-se de que você possui:

* Conhecimento sólido da linguagem Python (equivalente ao conteúdo do módulo "Python 1" ou similar).
* Noções básicas de HTML, CSS e JavaScript.
* Ambiente de desenvolvimento Python configurado (versão compatível com o Django utilizado no curso).
* Pip (gerenciador de pacotes Python) instalado.
* Git instalado (para clonar o repositório e versionar seu progresso).

---

## 🚀 Como Utilizar Este Repositório

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd nome-do-repositorio
    ```
3.  **Crie e ative um ambiente virtual** (recomendado):
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```
4.  **Instale as dependências** (geralmente listadas em um arquivo `requirements.txt` dentro de cada exercício ou no projeto principal):
    ```bash
    pip install -r requirements.txt
    # ou
    pip install django
    ```
5.  **Siga as instruções** específicas de cada pasta de exercício. Geralmente, cada exercício terá seu próprio `README.md` com detalhes sobre o que precisa ser feito.
6.  **Execute as migrações** (se aplicável):
    ```bash
    python manage.py migrate
    ```
7.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
8.  Acesse a aplicação no seu navegador, geralmente em `http://127.0.0.1:8000/`.

---

## 📁 Estrutura dos Diretórios (Sugestão)