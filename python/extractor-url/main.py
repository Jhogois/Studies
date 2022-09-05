# url = 'https://bytebank.com/exchange?quantity=100&originCurrency=real&destinyCurrency=dolar'
url = ' '

# URL Sanitization
url = url.replace(' ', '')

# URL Validation
if url == '':
    raise ValueError('Empity URL')

# Separete base and parameter
index_interrogation = url.find('?')
url_base = url[:index_interrogation]
url_parameters = url[index_interrogation+1:]
print(url_parameters)

# Search a parameter value
search_parameter = 'quantity'
index_parameter = url_parameters.find(search_parameter)
index_value = index_parameter + len(search_parameter) + 1
index_comercial_e = url_parameters.find('&', index_value)
if index_comercial_e == -1:
    value = url_parameters[index_value:]
else:
    value = url_parameters[index_value:index_comercial_e]
print(value)