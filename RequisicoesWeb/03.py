import requests

request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL').json()

print(request['USDBRL']['bid'])