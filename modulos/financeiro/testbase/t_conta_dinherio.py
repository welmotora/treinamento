from lib.dados.contadinheiro import DESCRICAO
from lib.dados.saldo import SALDO_INCIAL_ZERADO
from lib.dados.situacao import SITUACAO_ABERTA, SITUACAO_ENCERRADA, SITUACAO_FECHADA
from modulos.financeiro.formulario.f_conta_dinheiro import (
    conta_dinheiro_descricao,
    conta_dinheiro_salvar,
    conta_dinheiro_situacao,
    conta_dinherio_saldo_inicial,
)
from modulos.financeiro.testbase.t_conta_financeira import (
    criando_nova_conta_financiera_dinherio,
)
from modulos.login.testbase.t_login import logando_no_adaptei


def criar_conta_dinheiro():
    criando_nova_conta_financiera_dinherio()


def criar_conta_dinheiro_zerada(a_texto, b_texto, c_texto):
    criar_conta_dinheiro()
    conta_dinheiro_descricao(a_texto)
    conta_dinheiro_situacao(b_texto)
    conta_dinherio_saldo_inicial(c_texto)
    conta_dinheiro_salvar()


def criando_conta_dinheiro_aberta_zerada():
    criar_conta_dinheiro_zerada(DESCRICAO, SITUACAO_ABERTA, SALDO_INCIAL_ZERADO)


def criando_conta_dinheiro_fechada_zerada():
    criar_conta_dinheiro_zerada(DESCRICAO, SITUACAO_FECHADA, SALDO_INCIAL_ZERADO)


def criando_conta_dinheiro_encerrada_zerada():
    criar_conta_dinheiro_zerada(DESCRICAO, SITUACAO_ENCERRADA, SALDO_INCIAL_ZERADO)


def executar_testes_conta_dinheiro():
    logando_no_adaptei()
    criando_conta_dinheiro_aberta_zerada()
    criando_conta_dinheiro_fechada_zerada()
    criando_conta_dinheiro_encerrada_zerada()
