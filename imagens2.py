from PIL import ImageFilter, Image


imagem = Image.open(r'imagens\tidalwave_payoff_poster_brazil_caf2354b.jpeg')
imagem.show()
imagem = imagem.filter(ImageFilter.BLUR)
imagem.show()