from xpath.html import button
from xpath.renderer import to_xpath



x = to_xpath(button("Salve"))
print(x) 