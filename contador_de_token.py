import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
CHAVE_API_GOOGLE = os.getenv("GEMINI_API")

genai.configure(api_key=CHAVE_API_GOOGLE)

MODELO_FLASH = "gemini-2.5-flash"
MODELO_PRO = "gemini-2.5-pro"

CUSTO_ENTRADA_FLASH = 0.3
CUSTO_SAIDA_FLASH = 2.5

CUSTO_ENTRADA_PRO = 1.25
CUSTO_SAIDA_PRO = 10.0

model_flash = genai.get_model(f"models/{MODELO_FLASH}")
limite_modelo_flash = {
    "tokens_entrada": model_flash.input_token_limit,
    "tokens_saida": model_flash.output_token_limit
}

print(f"Os limites do modelo flash são: {limite_modelo_flash}")

model_pro = genai.get_model(f"models/{MODELO_PRO}")
limite_modelo_pro= {
    "tokens_entrada": model_pro.input_token_limit,
    "tokens_saida": model_pro.output_token_limit
}

print(f"Os limites do modelo pro são: {limite_modelo_pro}")

llm_flash = genai.GenerativeModel(
    f"models/{MODELO_FLASH}"
)

quantidade_tokens = llm_flash.count_tokens("O que é uma calça de shooping?")
print(f'A quantidade de tokens é: {quantidade_tokens}')

resposta = llm_flash.generate_content("O que é uma calça de shopping?")
tokens_prompt = resposta.usage_metadata.prompt_token_count
tokens_resposta = resposta.usage_metadata.candidates_token_count

custo_total_flash = (tokens_prompt * CUSTO_ENTRADA_FLASH / 1048576) + (tokens_resposta * CUSTO_SAIDA_FLASH / 65536)
print(f"O custo total do modelo flash é: {custo_total_flash}")

custo_total_pro = (tokens_prompt * CUSTO_ENTRADA_PRO / 1048576 ) + (tokens_resposta * CUSTO_SAIDA_PRO / 65536)
print(f"O custo total do modelo pro é: {custo_total_pro}")
