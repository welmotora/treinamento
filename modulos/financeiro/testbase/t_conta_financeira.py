from lib.dados.conta_financeira import CONTA_DINHERIO
from modulos.financeiro.formulario.f_conta_financeira import (
    nova_conta_financeira,
    tipo_de_conta_financeira,
)


def criar_conta_financeira(p_texto):
    nova_conta_financeira()
    tipo_de_conta_financeira(p_texto)


def criando_nova_conta_financiera_dinherio():
    criar_conta_financeira(CONTA_DINHERIO)
