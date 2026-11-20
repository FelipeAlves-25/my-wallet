# My Wallet: Monitor de Finanças

> 🚧 **Status do Projeto:** Em desenvolvimento

Uma aplicação web simples construída com **FastAPI** no back-end e renderização de templates dinâmicos no front-end utilizando **Jinja2**. Seu principal objetivo é garantir ao usuário uma interface simples e intuitiva para visualizar e gerenciar suas finanças, trazendo relatórios que possam otimizar seu gasto financeiro sem a necessidade de uso de planilhas.

## ✨ Funcionalidades atuais

- [x] Configuração inicial do servidor com FastAPI
- [x] Integração com templates Jinja2 e arquivos estáticos
- [x] Tela inicial (`Home`) implementada

## 🛠️ Tecnologias utilizadas

- **Python 3.15+**
- **FastAPI** (Framework web back-end)
- **Jinja2** (Motor de templates HTML)
- **Uvicorn** (Servidor ASGI)

## 🚀 Como executar localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/FelipeAlves-25/my-wallet.git
   cd my-wallet
   ```

2. **Instale as dependências e inicie o servidor de desenvolvimento:**
   ```bash
   uv sync
   uvicorn src.main:app --reload
   ```

3. **Acesse no navegador:**
   Abra `http://127.0.0.1:8000` para visualizar a tela inicial.

## 📝 Licença e autoria

Este projeto foi criado por Felipe Alves e está sob a licença GLP. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
