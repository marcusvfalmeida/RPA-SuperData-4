from PIL import Image
from google import genai

API_KEY = ''

client = genai.Client(api_key=API_KEY)

imagem = Image.open(r'C:\Users\11696\Downloads\RPA\imagens\tidalwave_payoff_poster_brazil_caf2354b.jpeg')

resposta = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=[
        'Descreva o nome dos filmes da pasta.',
        imagem
    ]
)

print(resposta.text)