import re

class ExtractorURL:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.url_validation()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def url_validation(self):
        if not self.url:
            raise ValueError('Empity URL')

        pattern_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/exchange')
        match = pattern_url.match(url)

        if not match:
            raise ValueError('THE URL IS NOT VALID.')

    def get_base_url(self):
        index_interrogation = self.url.find('?')
        url_base = self.url[:index_interrogation]
        return url_base

    def get_url_parameters(self):
        index_interrogation = self.url.find('?')
        url_parameters = self.url[index_interrogation+1:]
        return url_parameters

    def get_parameter_value(self, search_parameter):
        index_parameter = self.get_url_parameters().find(search_parameter)
        index_value = index_parameter + len(search_parameter) + 1
        index_comercial_e = self.get_url_parameters().find('&', index_value)
        if index_comercial_e == -1:
            value = self.get_url_parameters()[index_value:]
        else:
            value = self.get_url_parameters()[index_value:index_comercial_e]
        return value
    
    def __len__(self):
        return len(self.url)

    def __str__(self) -> str:
        return self.url + '\n' + 'Parameters: ' + self.get_url_parameters() + '\n' + 'Base URL: ' + self.get_base_url()

    def __eq__(self, __o: object) -> bool:
        return self.url == __o.url

url = 'bytebank.com/exchange?quantity=100&originCurrency=real&destinyCurrency=dolar'
url_extractor = ExtractorURL(url)
url_extractor2 = ExtractorURL(url)

dolar_value = 5.50
origin_currency = url_extractor.get_parameter_value("originCurrency")
destiny_currency = url_extractor.get_parameter_value("destinyCurrency")
quantity = url_extractor.get_parameter_value("quantity")

if origin_currency == "real" and destiny_currency == "dolar":
    conversion_value = int(quantity) / dolar_value
    print("The value of R$" + quantity + " is equal to US$" + str(conversion_value))
elif origin_currency == "dolar" and destiny_currency == "real":
    conversion_value = int(quantity) * dolar_value
    print("The value of US$" + quantity + " is equal to R$" + str(conversion_value))
elif origin_currency == destiny_currency:
    raise ValueError('Equal Currency. Please, select different currencies')
else:
    print(f"The exchange of {origin_currency} to {destiny_currency} isn't available.")


#print('The length of the URL is: ', len(url_extractor))
#print(url_extractor)

print(id(url_extractor))
print(id(url_extractor2))

#print(url_extractor == url_extractor2)

#quantity_value = url_extractor.get_parameter_value("quantity")
#print(quantity_value)