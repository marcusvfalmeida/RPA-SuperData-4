import requests

url = "https://publica.cnpj.ws/cnpj/82640558000104"

response = requests.request("GET", url)
# response = requests.get(url)

print(response.text)