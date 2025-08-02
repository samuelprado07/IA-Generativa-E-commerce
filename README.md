💡 Projeto com IA Generativa usando Gemini API
________________________________________
🔨 Funcionalidades do Projeto
Neste projeto, dei os primeiros passos no universo da IA Generativa utilizando a API do Gemini, explorando seu potencial para interpretação de linguagem natural.
Desenvolvi duas aplicações principais:

•	🛍️ Categorizador de Produtos
Classifica automaticamente os itens de um e-commerce com base em suas descrições.

•	💬 Analisador de Sentimentos
Analisa comentários de clientes, identificando se as avaliações são positivas, negativas ou neutras.
________________________________________
✔️ Técnicas e Tecnologias Utilizadas
•	🐍 Programação em Python

•	🌐 Consumo da API Gemini (Google)

•	📊 Leitura e manipulação de dados com arquivos CSV

•	🛠️ Criação de ambiente virtual com venv

•	🔐 Utilização de variáveis de ambiente com .env

________________________________________
🛠️ Como abrir e rodar o projeto
1.	Clone o repositório e abra no Visual Studio Code.
2.	Crie um ambiente virtual:

Para Windows: 
python -m venv venv-gemini-1 
python venv-gemini-1\Scripts\activate 
________________________________________

Para Mac/Linux:
 python3 -m venv venv-gemini-1 
source venv-gemini-1/bin/activate
________________________________________
Instale as dependências: 
pip install -r requirements.txt 
________________________________________
🔑 Configurar a chave da API Gemini Gere sua chave de API no Google AI Studio. 
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
GEMINI_API_KEY=SUA_CHAVE_AQUI
