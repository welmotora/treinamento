import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from modulo_geral.dados.tempo import *


def tempo_padrao():
    time.sleep(TEMPO_PADRAO)


def tempo_botao():
    time.sleep(TEMPO_BOTAO)


driver = webdriver.Chrome()


def url(p_texto):
    driver.maximize_window()
    tempo_padrao()
    driver.get(p_texto)


def escrita_find_element_id(p_elemento, p_texto):
    driver.find_element_by_id(p_elemento).send_keys(p_texto)
    tempo_padrao()


def click_find_element_xpath(p_elemento):
    driver.find_element_by_xpath(p_elemento).click()
    tempo_botao()


 