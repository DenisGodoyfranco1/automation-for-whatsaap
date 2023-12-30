from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
from selenium.webdriver.common.action_chains import ActionChains


service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")

time.sleep(80)

mensagem = """ Fala galera!!!
Quer tirar um dinheiro no final do ano 
segue o link abaixo --> 
"""

lista_contatos =["Denis filho","4 macacos","projeto fit","botzin","coisas de negocios","teste",]

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys("Denis filho")
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)
pyperclip.copy(mensagem)
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "v")
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)

qtde_contatos = len(lista_contatos)

if qtde_contatos % 5 == 0:
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1

for i in range(qtde_blocos):
    # rodar o codigo de encaminhar
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    # selecionar a mensagem para enviar e abre a caixa de encaminhar
    lista_elementos = nav.find_elements('class name', '_2AOIt')
    for item in lista_elementos:
        mensagem = mensagem.replace("\n", "")
        texto = item.text.replace("\n", "")
        if mensagem in texto:
            elemento = item

    ActionChains(nav).move_to_element(item).perform()
    item.find_element('class name', '_3u9t-').click()
    time.sleep(0.5)
    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    time.sleep(1)

    for nome in lista_enviar:
        # selecionar os 5 contatos para enviar
        # escrever o nome do contato
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(nome)
        time.sleep(1)
        # dar enter
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(1)
        # apagar o nome do contato
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        time.sleep(1)

    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(3)