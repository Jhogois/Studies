from multiprocessing.sharedctypes import Value
from validate_docbr import CNPJ
from validate_docbr import CPF

class Document:
   
    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Invalid number of digits!")

class DocCpf:
    def __init__(self, document) -> None:
        if self.validation(document):
            self.cpf = document
        else:
            raise ValueError("Invalid CPF!")

    def __str__(self) -> str:
        return self.format()

    def validation(self, document):
        validator = CPF()
        return validator.validate(document)

    def format(self):
        mask = CPF()
        return mask.mask(self.cpf)

class DocCnpj:
    def __init__(self, document) -> None:
        if self.validation(document):
            self.cnpj = document
        else:
            raise ValueError("Invalid CNPJ!")

    def __str__(self) -> str:
        return self.format()

    def validation(self, document):
        validator = CNPJ()
        return validator.validate(document)

    def format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)
