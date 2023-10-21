import requests
#import json

username = 'violiveiradev'
url = f'https://api.github.com/users/{username}'

r = requests.get(url)

print(r.status_code)
print(r.json())
print(r.text)
print(r.url)

print('Nome: ', r.json()['name'])
print('Nome de usuario: ', r.json()['login'])
print('Numero de repositórios públicos : ', r.json()['public_repos'])
print('Data de criação da conta : ', r.json()['created_at'])

#dados_user = json.loads(r.text)
#
#print('Nome: ', dados_user['name'])
#print('Nome de usuario: ', dados_user['login'])
#print('Numero de repositórios públicos : ', dados_user['public_repos'])
#print('Data de criação da conta : ', dados_user['created_at'])
