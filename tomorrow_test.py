# importando bibliotecas

import json
import requests

# variáveis para determinar a latitude e longitude do local

latitude = -23.55006
longitude = -46.63416

TOMORROW_API_KEY = '<<_KEY_>>' # Substituit pela chave da API obetida no Tomorrow.io
url = f"https://api.tomorrow.io/v4/weather/realtime?location={latitude},{longitude}&apikey={TOMORROW_API_KEY}" # URL para chamada da API

headers = {"accept": "application/json"}
response = requests.get(url, headers=headers) # variável que guarda o retorno da chamada da API

if response.status_code == 200: # código de status 200 representa houve sucesso na chamada
    data = response.json() # variável que guarda o retorno da chamada da API em formato JSON
    print(json.dumps(data, indent=4)) # exibe o resultado dachamada da API em formato JSON
else:
    print(f'Erro na requisição: {response.status_code}, mensagem: {response.json().get("message", "")}') # exibe mensagem em caso de erro da requisição