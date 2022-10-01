import requests

class FindAdress:
    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.cep_is_valid(cep):
            self.cep = cep
        else:
            raise ValueError("Invalid CEP")

    def __str__(self) -> str:
        return self.format_cep()

    def cep_is_valid(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    
    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
     
    def access_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json"
        r = requests.get(url)
        data = r.json()
        return (data['bairro'], data['localidade'], data['uf'])