from lib.dsl.liguagem import click_find_element_xpath, escrever_find_element_xpath
from lib.xpath.criar_placeholder import PESQUISAR
from lib.xpath.criar_xpath_botao import NOVA_CONTA_FINANCEIRA
from modulos.financeiro.elemento.e_conta_financeira import (
    SELECIONAR_CONTA,
    TIPO_DE_CONTA,
)


def nova_conta_financeira():
    click_find_element_xpath(NOVA_CONTA_FINANCEIRA)


def tipo_de_conta_financeira(p_texto):
    click_find_element_xpath(TIPO_DE_CONTA)
    escrever_find_element_xpath(PESQUISAR, p_texto)
    click_find_element_xpath(SELECIONAR_CONTA)
