from lib.dsl.liguagem import click_find_element_xpath, escrita_find_element_id
from lib.xpath.criar_xpath_botao import ENTRAR
from modulos.login.elemento.html_login import (
    PASSWORD,
    SELECIONAR_BANCO_DE_DADOS,
    USERNAME
)


def informar_usuario(ptexto):
    escrita_find_element_id(USERNAME, ptexto)


def informar_senha(ptexto):
    escrita_find_element_id(PASSWORD, ptexto)


def botao_entrar():
    click_find_element_xpath(ENTRAR)


def selecinar_banco_de_dados():
    click_find_element_xpath(SELECIONAR_BANCO_DE_DADOS)
