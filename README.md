# Clone do X (Twitter) - Projeto Final

Este projeto é um clone funcional da rede social X (antigo Twitter), desenvolvido como um monolito utilizando Python com a estrutura do Django Framework e estilização customizada no modo escuro (Super Black).

## 🚀 Funcionalidades Implementadas

- **Autenticação Completa**: Cadastro de novos usuários e sistema de login/logout seguro.
- **Linha do Tempo (Feed)**: Exibição dinâmica contendo as postagens do próprio usuário e das contas que ele segue.
- **Criação de Posts**: Campo de texto rápido para realizar novas publicações limitadas a 280 caracteres.
- **Interações Sociais**:
  - Mecanismo de curtir e descurtir publicações com atualização do contador.
  - Sistema de respostas (comentários) anexados a cada postagem.
  - Painel "Quem seguir" para gerenciar novos relacionamentos entre usuários.
- **Perfil do Usuário**: Página interna dedicada à alteração de credenciais e edição de dados de biografia.

## 🛠️ Tecnologias Utilizadas

- **Back-end & Front-end**: Python 3.12 + Django Framework (Monolito com Django Templates)
- **Banco de Dados**: SQLite3 (nativo do ambiente de desenvolvimento)
- **Estilização**: HTML5 / CSS3 customizado inspirado no layout moderno do X

## 🔧 Como Executar o Projeto Localmente

1. Clone o repositório para sua máquina local.
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Mac/Linux:
   source venv/bin/activate
   ```
3. Instale as dependências obrigatórias:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
6. Acesse a aplicação em seu navegador através do endereço `http://127.0.0`.
