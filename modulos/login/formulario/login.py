from modulo_geral.dsl.liguagem import click_find_element_xpath, escrita_find_element_id
from modulo_login.elemento.elementohtml_login import ENTRAR, PASSWORD, USERNAME


def informar_usuario(ptexto):
    escrita_find_element_id(USERNAME, ptexto)


def informar_senha(ptexto):
    escrita_find_element_id(PASSWORD, ptexto)


def clicando_no_botao_entrar():
    click_find_element_xpath(ENTRAR)
