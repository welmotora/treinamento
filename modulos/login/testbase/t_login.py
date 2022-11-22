from lib.dados.conexao import *
from lib.dados.login import *
from lib.dsl.liguagem import *
from modulos.login.formulario.f_login import *


def login_adaptei(p_url, p_usuario, p_senha):
    url(p_url)
    informar_usuario(p_usuario)
    informar_senha(p_senha)
    botao_entrar()
    selecinar_banco_de_dados()


def logando_no_adaptei():
    login_adaptei(CONECAO_APAPTEI, USUARIO, SENHA)
