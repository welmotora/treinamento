import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from lib.dados.tempo import *

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)


def tempo_padrao():
    time.sleep(TEMPO_PADRAO)


def tempo_botao():
    time.sleep(TEMPO_BOTAO)


def url(p_texto):
    driver.maximize_window()
    tempo_padrao()
    driver.get(p_texto)


def escrita_find_element_id(p_elemento, p_texto):
    driver.find_element(By.ID, p_elemento).send_keys(p_texto)
    tempo_botao()


def click_find_element_xpath(p_elemento):
    driver.find_element(By.XPATH, p_elemento).click()
    tempo_botao()


def escrever_find_element_xpath(p_elemento, ptexto):
    driver.find_element(By.XPATH, p_elemento).send_keys(ptexto)
    tempo_padrao()
