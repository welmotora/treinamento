from xpath.html import button

from xpath.renderer import to_xpath

USERNAME = "username"
PASSWORD = "password"
# ENTRAR = "//button[contains(.,'Entrar')]"
ENTRAR =  to_xpath(button("Entrar"))
