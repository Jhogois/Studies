import requests
from access_cep import FindAdress

cep = "12949091"
object_cep = FindAdress(cep) 

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(type(r.text))

bairro, cidade, uf = object_cep.access_via_cep()

print(bairro, cidade, uf)