from lib.dados.d_data import DATA_PADRAO
from lib.dsl.liguagem import *
from lib.xpath.criar_placeholder import (
    ENTRE_COM_A_DESCRICAO,
    PESQUISAR,
    SALDO_INCIAL,
    SELECIONE,
)
from lib.xpath.criar_xpath_botao import CANCELAR, SALVAR
from modulos.financeiro.elemento.e_conta_dinheiro import (
    COMBO_SITUACAO,
    SELECIONAR_SITUACAO,
)


def conta_dinheiro_descricao(p_texto):
    escrever_find_element_xpath(ENTRE_COM_A_DESCRICAO, p_texto)


def conta_dinheiro_situacao(p_texto):
    click_find_element_xpath(COMBO_SITUACAO)
    escrever_find_element_xpath(PESQUISAR, p_texto)
    click_find_element_xpath(SELECIONAR_SITUACAO)


def conta_dinherio_saldo_inicial(p_texto):
    escrever_find_element_xpath(SALDO_INCIAL, p_texto)


def conta_dinheiro_data_saldo_incial():
    click_find_element_xpath(SELECIONE)
    click_find_element_xpath(DATA_PADRAO)


def conta_dinheiro_salvar():
    click_find_element_xpath(SALVAR)


def conta_dinheiro_cancelar():
    click_find_element_xpath(CANCELAR)
