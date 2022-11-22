from modulo_geral.dados.conexao import *
from modulo_geral.dsl.liguagem import *
from modulo_login.dados.login import *
from modulo_login.formulario.formulario_login import *


def login_adaptei(p_url, p_usuario, p_senha):
    url(p_url)
    informar_usuario(p_usuario)
    informar_senha(p_senha)
    clicando_no_botao_entrar()


def logando_no_adaptei():
    login_adaptei(CONECAO_APAPTEI, USUARIO, SENHA)
