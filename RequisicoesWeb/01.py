import requests
import pandas as pd

ceps = open('ceps.txt','r').read().splitlines()
dados = []

# request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
# print(request.text)

for cep in ceps:
    request = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
    # print(request['logradouro'])
    dados.append(request)

df = pd.DataFrame(dados)
# print(df)
df.to_csv('ceps.csv')