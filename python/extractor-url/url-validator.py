'''
Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

Exemplos de URLs inválidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio

'''
# https://www.bytebank.com.br/cambio
import re

url = 'http://www.bytebank.com.br/cambio'
pattern_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = pattern_url.match(url)

if not match:
    raise ValueError('THE URL IS NOT VALID.')

print('THE URL IS VALID')







