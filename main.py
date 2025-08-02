import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API")
genai.configure(api_key=CHAVE_API_GOOGLE)
modelo= "gemini-2.5-flash"

prompt_sistema = "Liste apenas os nomes dos produtos, e ofereça uma breve descrição."

configuracao_modelo = {
    "temperature": 2.0,
    "top_p": 0.9,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

llm= genai.GenerativeModel(
    model_name = modelo,
    system_instruction = prompt_sistema,
    generation_config=configuracao_modelo)       

pergunta = "Liste 3 produtos de moda sustentável para ir ao shopping"

resposta = llm.generate_content(pergunta)
print(f'A resposta gerada para pergunta é: Aqui estão os 3 produtos de moda sustentável para você comprar')
print(resposta.text)
