from xpath.html import button
from xpath.renderer import to_xpath

NOVA_CONTA_FINANCEIRA = to_xpath(button("Nova conta"))
ENTRAR = to_xpath(button("Entrar"))
SALVAR = to_xpath(button("Salvar"))
CANCELAR = to_xpath(button("Cancelar"))
