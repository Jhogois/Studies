class LeitorDeArquivo:
    def __init__(self, arquivo) -> None:
        self.arquivo = arquivo
        print(f'Abrindo aquivo: {self.arquivo}')

    def ler_proxima_linha(self):
        raise IOError
        print('Lendo linha...')
        return 'Linha de arquivo'

    def fechar(self):
        print('Fechando arquivo.')

    def __enter__(self):
        return self

    def __exit__(self, type, valor, traceback):
        print('Fechando arquivo.')