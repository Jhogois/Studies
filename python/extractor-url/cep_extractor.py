adress = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"


import re #Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

pattern = re.compile('[0-9]{5}[-]?[0-9]{3}')
search = pattern.search(adress) #Match 
if search:
    cep = search.group()
    print(cep)