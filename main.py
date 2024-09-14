import requests

# requisitando o endpoint

link = 'http://localhost:5000/totalvendas'

requisicao = requests.get(link) # to querendo pegar info da api

print(requisicao) # vai printar 200, codigo de sucesso
print(requisicao.json) # dict la do codigo, a partir de um dict vc pode usar todas funcoes dicts do py nele

dicionario = requisicao.json

print(dicionario['total_vendas'])