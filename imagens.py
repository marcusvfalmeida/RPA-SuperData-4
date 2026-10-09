from PIL import Image, ImageDraw, ImageFont
import os

PATH = r'C:\Users\11696\Downloads\RPA\imagens'
# imagem = Image.open(r'imagens\Deadpool_2016.jpg')
# imagem = imagem.resize((1400,1400))

for arquivo in os.listdir(PATH):
    imagem = Image.open(rf'{PATH}/{arquivo}')
    imagem = imagem.convert(mode='L')
    imagem = imagem.rotate(90, expand=True)
    draw = ImageDraw.Draw(imagem)
    draw.text((10, 10), arquivo, fill=('black'))
    imagem.save(rf'{PATH}/CONVERTIDO {arquivo}')

# imagem.show()