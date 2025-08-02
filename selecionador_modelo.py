import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
CHAVE_API_GOOGLE = os.getenv("GEMINI_API")

genai.configure(api_key=CHAVE_API_GOOGLE)
modelo= "gemini-2.5-flash"

def carrega(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f'Erro ao carregar arquivo: {e}')

prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("dados\lista_clientes.csv")

modelo_flash = genai.GenerativeModel(f'models/{modelo}')
qtd_tokens = modelo_flash.count_tokens(prompt_usuario)

limite_tokens = 3000

if qtd_tokens.total_tokens >= limite_tokens:
    modelo = "gemini-2.5-pro"

print(f"O modelo selecionado foi: {modelo}")

llm = genai.GenerativeModel(
    model_name= modelo,
    system_instruction= prompt_sistema
)

resposta = llm.generate_content(prompt_usuario)
print(f'Resposta: {resposta.text}')