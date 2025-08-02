import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API")
genai.configure(api_key=CHAVE_API_GOOGLE)
modelo= "gemini-2.5-flash"

def categorizarProduto(nome_produto, lista_categorias_possiveis):
    prompt_sistema = f"""
                Você é um categorizador de produtos.
                Você deve assumir as categorias presentes na lista abaixo.

                # Lista de Categorias Válidas
                {lista_categorias_possiveis.split(",")}

                # Formato da Saída
                Produto: Nome do Produto
                Categoria: apresente a categoria do produto

                # Exemplo de Saída
                Produto: Escova elétrica com recarga solar
                Categoria: Eletrônicos Verdes
                    """

    llm= genai.GenerativeModel(
        model_name= modelo,
        system_instruction= prompt_sistema
    )

    resposta= llm.generate_content(nome_produto)
    return resposta.text

def main():

    produto = input("Informe o produto que você deseja classificar:")

    lista_categorias_possiveis = "Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza Ecológicos,Alimentos Orgânicos, Produtos de higiene sustentáveis."
    while produto != "":
        print(f'Resposta: {categorizarProduto(produto,lista_categorias_possiveis)}')
        produto = input("Informe o produto que você deseja classificar:")


if __name__ == "__main__":
    main()