from modulos.financeiro.formulario.f_conta_dinheiro import *
from modulos.login.testbase.t_login import logando_no_adaptei
from modulos.financeiro.testbase.t_conta_financeira import criando_nova_conta_financiera_dinherio
from lib.dados.situacao import SITUAÇAO_ABERTA, SITUAÇAO_FECHADA, SITUAÇAO_ENCERRADA
from lib.dados.conta_dinheiro import DESCRICAO
from lib.dados.saldo import SALDO_INCIAL_ZERADO, SALDO_INCIAL_POSITIVO

def criar_conta_dinheiro():
    criando_nova_conta_financiera_dinherio()

def criar_conta_dinheiro_zerada(a_texto,b_texto,c_texto):
    criar_conta_dinheiro()
    conta_dinheiro_descricao(a_texto)
    conta_dinheiro_situacao(b_texto)
    conta_dinherio_saldo_inicial(c_texto)
    conta_dinheiro_salvar()
    

def criando_conta_dinheiro_aberta_zerada():
    criar_conta_dinheiro_zerada(DESCRICAO, SITUAÇAO_ABERTA, SALDO_INCIAL_ZERADO)

def criando_conta_dinheiro_fechada_zerada():
    criar_conta_dinheiro_zerada(DESCRICAO, SITUAÇAO_FECHADA, SALDO_INCIAL_ZERADO)
    
def criando_conta_dinheiro_encerrada_zerada():
    criar_conta_dinheiro_zerada(DESCRICAO, SITUAÇAO_ENCERRADA, SALDO_INCIAL_ZERADO)
    
def executar_testes_conta_dinheiro():
    logando_no_adaptei()
    criando_conta_dinheiro_aberta_zerada()
    criando_conta_dinheiro_fechada_zerada()
    criando_conta_dinheiro_encerrada_zerada()

