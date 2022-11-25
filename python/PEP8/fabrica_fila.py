from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioriataria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioriataria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioriataria()

        else:
            raise NotImplementedError('Tipo de fila não existe')
