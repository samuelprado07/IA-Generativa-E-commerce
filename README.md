💡 Projeto com IA Generativa usando Gemini API

🔨 Funcionalidades do Projeto

Neste projeto, dei os primeiros passos no universo da IA Generativa utilizando a API do Gemini. Desenvolvi duas aplicações principais:

- Categorizador de produtos para um e-commerce, capaz de classificar automaticamente os itens com base em suas descrições.

- Analisador de sentimentos de comentários de clientes, permitindo identificar se as avaliações são positivas, negativas ou neutras.

✔️ Técnicas e Tecnologias Utilizadas

- Programação em Python

- Consumo da API Gemini (Google)

- Leitura e manipulação de dados com arquivos CSV

- Criação de ambiente virtual com venv

- Utilização de variáveis de ambiente com .env

🛠️ Como abrir e rodar o projeto

- Clone o repositório e abra no Visual Studio Code.

- Crie um ambiente virtual:

Para Windows:

python -m venv venv-gemini-1

venv-gemini-1\Scripts\activate

Para Mac/Linux:

python3 -m venv venv-gemini-1

source venv-gemini-1/bin/activate


Instale as dependências: pip install -r requirements.txt


🔑 Configurar a chave da API Gemini

Gere sua chave de API no Google AI Studio.

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo: 
GEMINI_API_KEY=SUA_CHAVE_AQUI


