import requests

url = "http://192.168.3.57:5001/test"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("Erro na requisição: código de status " + str(response.status_code))
